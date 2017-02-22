'''
Collection of utilities for the loggers
'''

from uuid import uuid4
import logging
import os
import json
from flask import request


class CustomFilter(logging.Filter):
    '''
    Filters the input of the loggers
    '''

    def _get_request_body(self):
        if request.form:
            return request.form.keys()[0]
        return {}

    def _map_headers(self, item):
        return item

    def _get_x_list_param(self, name):
        if request.headers.getlist(name):
            return request.headers.getlist(name)[0]
        return ''

    def filter(self, log_record):
        log_record.host = request.url_root
        log_record.uri = request.path
        log_record.method = request.method
        log_record.remote_host = request.environ.get('REMOTE_ADDR')
        log_record.remote_port = request.environ.get('REMOTE_PORT')
        log_record.x_forwarded_for = self._get_x_list_param('X-FORWARDED-FOR')
        log_record.x_forwarded_proto = self._get_x_list_param('X-FORWARDED-PROTO')
        log_record.body = self._get_request_body()
        log_record.request_id = str(uuid4())
        log_record.headers = {k: self._map_headers(v) for k, v in request.headers.iteritems()}
        log_record.environment = os.environ.get('ENVIRONMENT', 'development')
        log_record.app_id = os.environ.get('APP_ID', '')
        log_record.instance_id = os.environ.get('INSTANCE_ID', '')
        log_record.instance_type = os.environ.get('INSTANCE_TYPE', '')
        log_record.instance_number = os.environ.get('INSTANCE_NUMBER', '')
        log_record.commit_id = os.environ.get('COMMIT_ID', '')

        return True


class CustomFormatter(logging.Formatter):
    '''
    Format the output of the loggers
    '''

    # To remove the other attributes of the record
    BLACKLIST = [
        'relativeCreated',
        'process',
        'module',
        'funcName',
        'filename',
        'levelno',
        'processName',
        'lineno',
        'args',
        'exc_text',
        'thread',
        'created',
        'threadName',
        'msecs',
        'pathname',
        'exc_info'
    ]

    def format(self, record):
        properties = dict((key, value) for key, value in vars(record).iteritems() if key not in CustomFormatter.BLACKLIST)

        record.msg = json.dumps(properties)

        return super(CustomFormatter, self).format(record)
