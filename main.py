import asyncio

from aiogram import Bot, Dispatcher
from config.bot_config import BOT_TOKEN
from utils.logger import get_logger
from handlers.commands.base_handlers import base_handlers
from handlers.custom_handlers.join_handlers import join_router
from config.bot_config import client
from handlers.custom_handlers.custom_commands import filters_router


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
logger = get_logger(__name__)
dp.include_routers(
    base_handlers,
    filters_router,
    join_router,
)


async def start_telethon():
    """Запуск Telethon клиента"""
    try:
        # Проверяем есть ли файл сессии
        import os
        if not os.path.exists('config/secure_session.session'):
            logger.warning("Файл сессии не найден. Нужна авторизация.")

        await client.start()

        if await client.is_user_authorized():
            me = await client.get_me()
            logger.info(f"✅ Telethon авторизован как: {me.first_name} (@{me.username})")
            return True
        else:
            logger.error("❌ Telethon не авторизован")
            return False

    except Exception as e:
        logger.error(f"Ошибка запуска Telethon: {e}", exc_info=True)
        return False


async def main():
    logger.info('Запуск системы...')

    try:
        telethon_success = await start_telethon()

        if not telethon_success:
            logger.warning("Мониторинг чатов отключен из-за ошибки авторизации")

        logger.info('Запуск Aiogram бота...')
        await dp.start_polling(bot)

    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)
    finally:
        await bot.session.close()
        if client and client.is_connected():
            await client.disconnect()
        logger.info('Бот остановлен')


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Остановка по команде пользователя")
    except Exception as e:
        logger.error(f"Ошибка: {e}")