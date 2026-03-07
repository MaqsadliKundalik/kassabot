from aiogram import Router
from aiogram.types import Message, user
from aiogram.filters import Command
from models.main import Report, User
from aiogram.fsm.context import FSMContext
from config import KASSA_CHAT_ID
from keyboards import vote_btn
from states import ReportStates

router = Router()

@router.message(Command("reports"))
async def reports(message: Message, state: FSMContext):
    await state.set_state(ReportStates.caption)
    await message.answer("Kassadan nima uchun pul olmoqchisiz?")
    
@router.message(ReportStates.caption)
async def caption(message: Message, state: FSMContext):
    await state.update_data(caption=message.text)
    await state.set_state(ReportStates.price)
    await message.answer("Summani kiriting:")
    
@router.message(ReportStates.price)
async def price(message: Message, state: FSMContext, user: User):
    data = await state.get_data()
    report = Report(
        user_id=message.from_user.id,
        caption=data["caption"],
        price=message.text
    )
    await message.bot.send_message(
        chat_id=KASSA_CHAT_ID, 
        text=f"<b>Yangi ariza:</b>\n\nRaqami: {report.id}\nArizachi: {user.name}\n\n{report.caption}\n\nSumma: {report.price}",
        reply_markup=vote_btn(report_id=report.id),
        parse_mode="HTML"
    )
    await report.save()
    await message.answer("✅ Ariza muvaffaqiyatli yuborildi!")
    await state.clear()
