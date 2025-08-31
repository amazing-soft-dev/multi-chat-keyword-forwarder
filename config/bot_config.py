import os
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession

from utils.logger import get_logger


logger = get_logger(__name__)


#load_dotenv() УБРАТЬ ПЕРЕД ЗАПУСКОМ СЕРВЕРА!!

BOT_TOKEN = os.getenv('BOT_TOKEN')

ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')
ALLOWED_USERS = [int(user_id) for user_id in os.getenv('ALLOWED_USERS').split(',')]

API_ID =  int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
SESSION = os.getenv('SESSION')

session = StringSession(SESSION)

client = TelegramClient(
    session=session,
    api_id=API_ID,
    api_hash=API_HASH,
    device_model="iPhone 13 Pro",
    system_version="14.8.1",
    app_version="10.2.5"
)