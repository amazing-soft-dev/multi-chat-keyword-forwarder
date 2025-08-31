from config.bot_config import ALLOWED_USERS


def is_user_allowed(user_id: int) -> bool:
    """Проверяет, есть ли у пользователя доступ к боту"""
    return user_id in ALLOWED_USERS


def clean_links(links: list) -> list:
    cleaned = []
    for link in links:
        if link.startswith('https://t.me/'):
            link = link.split('/')[-1]
        elif link.startswith('@'):
            link = link[1:]
        cleaned.append(link.strip())
    return cleaned