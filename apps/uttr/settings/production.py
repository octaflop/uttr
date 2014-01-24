from .base import *

from os import environ

DEBUG = True
TEMPLATE_DEBUG = DEBUG

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_HOST_USER = 'faris@theluckybead.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[Digital Textbook Study] '
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'digitaltextbookstudy@gmail.com'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.normpath(os.path.join("/", "tmp", "whoosh_index")),
    }
}

WSGI_APPLICATION = 'uttr.wsgi.production'


try:
    from local_settings import *
except:
    pass
