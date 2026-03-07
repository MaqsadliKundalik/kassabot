from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import main_menu

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Salom, men kassadan pul olish uchun ariza yuborishingizda yordam beraman..", reply_markup=main_menu)
    