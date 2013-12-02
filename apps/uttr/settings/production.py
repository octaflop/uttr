from .base import *

from os import environ

#DB_PASS = environ['DB_PASS']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'uttrdb',
        'USER': 'uttr',
        #'PASSWORD': DB_PASS,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

WSGI_APPLICATION = 'uttr.wsgi.production'

DEBUG = False

TEMPLATE_DEBUG = DEBUG

try:
    from local_settings import *
except:
    pass
