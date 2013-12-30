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

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.normpath(os.path.join("/", "tmp", "whoosh_index")),
    }
}

WSGI_APPLICATION = 'uttr.wsgi.production'

DEBUG = True

TEMPLATE_DEBUG = DEBUG

try:
    from local_settings import *
except:
    pass
