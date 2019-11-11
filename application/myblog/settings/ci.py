from application.myblog.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'root',
        'PASSWORD': 'docker',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}