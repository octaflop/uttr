from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'uttr',
        'PASSWORD': 'uttr_pass',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

WSGI_APPLICATION = 'uttr.wsgi.production'

