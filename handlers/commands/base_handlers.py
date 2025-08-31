from datetime import datetime
from aiogram import Router
from aiogram.enums import ChatType
from aiogram.filters import CommandStart
from aiogram.types import Message
from telethon import events

from utils.json_keywords_manager import keywords_manager
from utils.logger import get_logger
from utils.special_func import is_user_allowed
from config.bot_config import client


logger = get_logger(__name__)
base_handlers = Router()



@base_handlers.message(CommandStart())
async def start_command(message: Message):
    """Обработчик команды /start"""
    if message.chat.type != ChatType.PRIVATE:
        logger.warning(f"Попытка вызвать /start в чате {message.chat.id}")
        return

    if not is_user_allowed(message.from_user.id):
        await message.answer("⛔ Доступ запрещён.")
        return

    await message.answer(
        "👋 Привет! Я бот для мониторинга чатов.\n"
        "Доступные команды:\n"
        "/filters — показать и изменить ключевые слова\n"
        "/ban — показать и изменить бан слова\n\n"
        "Я автоматически ищу сообщения с ключевыми словами и присылаю их тебе."
    )
    logger.info(f"Пользователь {message.from_user.id} запустил /start")


@client.on(events.NewMessage(incoming=True, func=lambda e: not e.is_private))
async def keyword_monitor(event):
    """Мониторинг сообщений в чатах на ключевые слова"""

    try:
        chat = await event.get_chat()
        my_participant = await client.get_permissions(chat, 'me')
        if not my_participant:
            return
    except Exception as e:
        logger.debug(e)
        return

    try:
        logger.debug(f"Получено сообщение: {event.raw_text[:50]}...")

        text = event.raw_text.lower() if event.raw_text else ""

        filters = keywords_manager.get_keywords()
        ban_words = keywords_manager.get_ban_words()

        found_ban_words = [word for word in ban_words if word.lower() in text]
        if found_ban_words:
            return

        found_keywords = [word for word in filters if word.lower() in text]
        if not found_keywords:
            return


        if not found_keywords:
            return

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        chat = await event.get_chat()
        sender = await event.get_sender()

        chat_id = event.chat_id
        message_id = event.id
        message_link = f"https://t.me/c/{str(chat_id).replace('-100', '')}/{message_id}"

        report = (
            "==============================\n"
            f"📅 Дата: {date}\n\n"
            f"💬 Чат: {chat.title if hasattr(chat, 'title') else 'Private Chat'}\n"
            f"✉️ Сообщение:\n{event.raw_text}\n\n"
            f"🔍 Ключевые слова: {', '.join(found_keywords)}\n"
            f"👤 Отправитель: {sender.first_name} {getattr(sender, 'last_name', '') or ''}\n"
            f"📱 Username: @{sender.username if hasattr(sender, 'username') and sender.username else 'N/A'}\n"
            f"🆔 User ID: {sender.id}\n"
            f"🔗 Ссылка: {message_link}\n"
            "=============================="
        )


        await client.send_message(
            entity='me',
            message=report,
            link_preview=False
        )

        logger.info(f"Найдено ключевое слово в чате {chat_id}")

    except Exception as e:
        logger.error(f"Ошибка при обработке сообщения: {e}", exc_info=True)



