import sys
import os
from dotenv import load_dotenv


api_id = api_id
api_hash = api_hash
phone_number = phone_number
client = TelegramClient('session_' + phone_number, api_id, api_hash)
