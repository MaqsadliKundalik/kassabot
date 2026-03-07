from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from asyncio import run
from middlewares.users import UserMiddleware
from handlers import router
from logging import basicConfig, INFO

basicConfig(level=INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.update.middleware(UserMiddleware())
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    run(main())
