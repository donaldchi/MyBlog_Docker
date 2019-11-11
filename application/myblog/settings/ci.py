from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'circle_test',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
