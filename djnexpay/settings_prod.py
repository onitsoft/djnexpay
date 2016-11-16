from djnexpay.settings_base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nexpay',
        'USER': 'nexpay',
        'PASSWORD': os.environ.get('PSQL_PASS'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = [
    'nexpay.co',
    'www.nexpay.co',
    'api.nexpay.co'
]

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
