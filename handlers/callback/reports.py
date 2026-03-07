from aiogram import Router, F
from aiogram.types import CallbackQuery
from models.main import Report, User, ReportVote
from config import KASSA_CHAT_ID, ADMINS
from keyboards import vote_btn, more_view_btn

router = Router()

@router.callback_query(F.data.startswith("vote_"))
async def handle_report_vote(callback: CallbackQuery, user: User):
    report_id = int(callback.data.split("_")[-1])
    report = await Report.get_or_none(id=report_id)
    if not report:
        await callback.answer("Ariza topilmadi")
        return
    choice = callback.data.split("_")[1]
    
    exists = await ReportVote.filter(report=report, user=user).first()
    if exists:
        await exists.delete()
    
    await ReportVote.create(report=report, user=user, vote=choice)

    yes_votes = await ReportVote.filter(report=report, vote="yes").count()
    no_votes = await ReportVote.filter(report=report, vote="no").count()
    
    if yes_votes + no_votes == 5:
        if yes_votes >= 3:
            for admin_id in ADMINS:
                await callback.bot.send_message(admin_id, f"✅ Ariza {report.id} yetarlicha ovoz yig'di", reply_markup=more_view_btn(report_id=report.id))
        else:
            for admin_id in ADMINS:
                await callback.bot.send_message(admin_id, f"❌ Ariza {report.id} yetarlicha ovoz yig'madi", reply_markup=more_view_btn(report_id=report.id))


    await callback.message.edit_reply_markup(reply_markup=vote_btn(report.id, yes_votes, no_votes))
    await callback.answer()


@router.callback_query(F.data.startswith("more_"))
async def handle_more_view(callback: CallbackQuery):
    report_id = int(callback.data.split("_")[-1])
    report = await Report.get_or_none(id=report_id)
    if not report:
        await callback.answer("Ariza topilmadi")
        return
    await report.fetch_related("user")

    yes_count = await ReportVote.filter(report=report, vote="yes").count()
    no_count = await ReportVote.filter(report=report, vote="no").count()
    await callback.message.edit_text(f"<b>Ariza {report.id}</b>:\nArizachi: {report.user.name}\n\n{report.caption}\n\nSumma: {report.price}\n✅ {yes_count}  ❌ {no_count}", parse_mode="HTML")
    await callback.answer()

