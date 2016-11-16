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
