"""
Log handler and initialize
"""
import logging
from logging.handlers import RotatingFileHandler
# from .commons import LOG_FILE_PATH, LOGGING_DEFAULT_LEVEL
from .commons import LOG_FILE_PATH, LOG_DEFAULT_LEVEL


def initialize_log(level=None):
    """initializing log"""
    logger = logging.getLogger()
    if level == 'debug':
        level = logging.DEBUG
    elif level == 'warning':
        level = logging.WARN
    elif level == 'error':
        level = logging.ERROR
    else:
        level = logging.INFO
    logger.setLevel(level)

    # file handler
    file_handler = RotatingFileHandler(LOG_FILE_PATH)
    file_handler.setLevel(logging.DEBUG)
    fmt = logging.Formatter('%(asctime)-10s %(levelname)8s ---\
         %(filename)10s.%(funcName)s: %(message)s')
    file_handler.setFormatter(fmt)

    # console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    # console_handler.setFormatter(
    #     logging.Formatter(logging.BASIC_FORMAT)
    # )
    console_handler.setFormatter(logging.Formatter(
        '[%(levelname)-20s]: %(message)s'))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logging.debug("LOG initialized")


initialize_log()
