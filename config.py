from dotenv import load_dotenv
import os
from datetime import datetime, timezone, timedelta

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = list(map(int, os.getenv("ADMINS").split(","))) if os.getenv("ADMINS") else []
KASSA_CHAT_ID = os.getenv("KASSA_CHAT_ID")

# Toshkent timezone (UTC+5)
TASHKENT_TZ = timezone(timedelta(hours=5))

def get_tashkent_time():
    """Toshkent vaqtini olish"""
    return datetime.now(TASHKENT_TZ)