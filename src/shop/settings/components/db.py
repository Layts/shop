"""Модуль конфигурации Базы Данных."""

import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'shop_dev'),
        'USER': os.getenv('POSTGRES_USER', 'shop_dev'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'shop_dev'),
        'HOST': os.getenv('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    },
}
