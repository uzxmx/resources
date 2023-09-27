import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler

def create_logger(log_name: str, log_dir: str = None, debug: bool = False):
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO if not debug else logging.DEBUG)

    log_fmt = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s - %(message)s')

    if log_dir:
        file_handler = TimedRotatingFileHandler(
                filename=os.path.join(log_dir, f'{log_name}.log'),
                when='midnight',
                interval=1,
                )
        file_handler.suffix = '%Y%m%d'
        file_handler.setFormatter(fmt=log_fmt)
        logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(fmt=log_fmt)
    logger.addHandler(stream_handler)

    return logger
