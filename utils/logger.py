import logging.config
from config.logger_config import log_dict_config


logging.config.dictConfig(log_dict_config)
logger = logging.getLogger('bot_logger')


def get_logger(name=None):
    """Возвращает настроенный дочерний логер"""
    return logger.getChild(name) if name else logger

