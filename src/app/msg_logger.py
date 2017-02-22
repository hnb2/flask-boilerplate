'''
General message logger
LOGENTRIES_TOKEN is set: send to logentries, else send to STDOUT
'''

import logging
import os
from logentries import LogentriesHandler
from app.util_logger import CustomFilter, CustomFormatter


def init():
    '''
    Registers the msg-logger
    '''
    handler = None
    if os.environ.get('LOGENTRIES_TOKEN') is not None:
        handler = LogentriesHandler(
            os.environ.get('LOGENTRIES_TOKEN'), format=CustomFormatter()
        )
    else:
        handler = logging.StreamHandler()
        handler.setFormatter(CustomFormatter())

    logger = logging.getLogger('msg-logger')
    logger.setLevel(logging.INFO)
    logger.addFilter(CustomFilter())
    logger.addHandler(handler)
