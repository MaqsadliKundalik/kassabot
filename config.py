from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS").split(",") if os.getenv("ADMINS") else []
KASSA_CHAT_ID = os.getenv("KASSA_CHAT_ID")