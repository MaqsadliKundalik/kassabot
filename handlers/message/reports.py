from aiogram import Router, F
from aiogram.types import Message, user
from aiogram.filters import Command
from models.main import Report, User
from aiogram.fsm.context import FSMContext
from config import KASSA_CHAT_ID
from keyboards import vote_btn
from states import ReportStates

router = Router()

@router.message(F.text == "Ariza berish")
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
    price_text = message.text.strip()
    
    cleaned_price = price_text.replace(' ', '').replace(',', '')
    
    if not cleaned_price.replace('.', '').isdigit():
        await message.answer("❌ Noto'g'ri format! Iltimos, faqat son kiriting (masalan: 50000, 50 000, 50.500)")
        return
    
    try:
        if '.' in cleaned_price:
            parts = cleaned_price.split('.')
            if len(parts) > 2:
                await message.answer("❌ Noto'g'ri format! Iltimos, faqat bitta nuqta ishlating (masalan: 50.500)")
                return
            
            whole_part = parts[0] if parts[0] else '0'
            decimal_part = parts[1] if len(parts) > 1 else '0'
            
            if len(decimal_part) > 2:
                price_value = int(whole_part + decimal_part)
            else:
                whole = int(whole_part) if whole_part else 0
                tiyin = int(decimal_part.ljust(2, '0')[:2])
                price_value = whole * 100 + tiyin
        else:
            price_value = int(cleaned_price)
        
        if price_value <= 0:
            await message.answer("❌ Summa musbat son bo'lishi kerak! Iltimos, qaytadan kiriting:")
            return
            
    except ValueError:
        await message.answer("❌ Noto'g'ri format! Iltimos, faqat son kiriting (masalan: 50000, 50 000, 50.500)")
        return
    
    data = await state.get_data()
    report = Report(
        user=user,
        caption=data["caption"],
        price=price_value
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
