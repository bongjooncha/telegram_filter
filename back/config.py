from dotenv import load_dotenv
import os

from telethon.sync import TelegramClient

load_dotenv()

class Config:
    TELEGRAM_ID = os.getenv('telegram_id')
    TELEGRAM_HASH = os.getenv('telegram_hash')
    TELEGRAM_PHONE = os.getenv('telegram_phone')
    CLIENT_NAME = TelegramClient('session_' + TELEGRAM_PHONE, TELEGRAM_ID, TELEGRAM_HASH)

