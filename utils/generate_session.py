import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from config.bot_config import API_ID, API_HASH


async def export_session():

    client = TelegramClient(StringSession(), API_ID, API_HASH)

    await client.start()

    if await client.is_user_authorized():
        print("=" * 50)
        print("✅ Сессия экспортирована!")
        print("SESSION_STRING:", client.session.save())
        print("=" * 50)

        me = await client.get_me()
        print(f"Авторизован как: {me.first_name} (@{me.username})")
    else:
        print("❌ Сначала авторизуйтесь в Telegram")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(export_session())