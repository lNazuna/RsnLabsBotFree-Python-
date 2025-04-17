import logging

def setup_logger():
    logger = logging.getLogger("discord_bot")
    logger.setLevel(logging.INFO)  # Definindo o nível de log como INFO para capturar mensagens INFO e acima

    # Criando um handler para salvar os logs em um arquivo
    file_handler = logging.FileHandler('bot.log', encoding='utf-8', mode='w')
    file_handler.setLevel(logging.INFO)  # Filtra mensagens de log INFO ou superior

    # Criando um handler para exibir os logs no console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Exibe mensagens de log INFO ou superior no console

    # Definindo o formato das mensagens de log
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Adicionando os handlers ao logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
