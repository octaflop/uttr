from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'uttr.db'),
    }
}

WSGI_APPLICATION = 'uttr.wsgi.dev.application'
