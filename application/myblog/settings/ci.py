from .base import *

ALLOWED_HOSTS = ['127.0.0.1']

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
