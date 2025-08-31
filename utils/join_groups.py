from telethon.tl.functions.channels import JoinChannelRequest
import time
from config.bot_config import client


def join_groups(group_list: list):
    count = 0
    with client:
        for channel in group_list:
            try:
                result = client.loop.run_until_complete(
                    client(JoinChannelRequest(channel))
                )
                print(f"Успешно: {channel}. Результат: {result}")
                count += 1
                time.sleep(60)  # Увеличенная задержка
            except Exception as e:
                print(f"❌ Ошибка в {channel}: {str(e)}")
                time.sleep(60)
    client.disconnect()
    return count


