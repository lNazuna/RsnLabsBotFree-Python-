import logging

def setup_logger():
    logger = logging.getLogger("discord_bot")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('bot.log', encoding='utf-8', mode='w')
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
