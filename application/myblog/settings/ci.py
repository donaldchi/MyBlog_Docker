from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'root',
        'PASSWORD': 'docker',
        'PORT': '3306',
    }
}
