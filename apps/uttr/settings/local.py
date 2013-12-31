from .base import *

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/uttr-messages'
DEFAULT_FROM_EMAIL = 'digitaltextbookstudy@zaneprep.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', '..', 'uttr.db'),
    }
}

WSGI_APPLICATION = 'uttr.wsgi.dev.application'

