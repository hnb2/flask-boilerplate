import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

ERROR_404_HELP = False

RESTPLUS_MASK_SWAGGER = False

# Environment based variables below

DEBUG = os.environ.get('DEBUG', True)

SECRET_KEY = os.environ.get('SECRET_KEY', '9oup6z5mdbw)8(f5$9ob@m&xha*(5ulqot&x*y1n$1^^9qo#d-')

APP_NAME = os.environ.get('APP_NAME', 'flask-boilerplate')

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'staging')

APP_TOKEN = os.environ.get('APP_TOKEN', '4b6f204b-04e8-489a-9aec-7d204e4cec34')

ROLLBAR_ACCESS_TOKEN = os.environ.get('ROLLBAR_ACCESS_TOKEN', None)
