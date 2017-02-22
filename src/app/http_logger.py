'''
HTTP logger sending to STDOUT
'''

import logging
from app.util_logger import CustomFilter, CustomFormatter


def init():
    '''
    Registers the http-logger
    '''
    handler = logging.StreamHandler()
    handler.setFormatter(CustomFormatter())

    logger = logging.getLogger('http-logger')
    logger.setLevel(logging.INFO)
    logger.addFilter(CustomFilter())
    logger.addHandler(handler)
