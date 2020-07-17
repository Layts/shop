"""Общий модуль конфигурации."""

import os


BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)),
))

SRC_DIR = os.path.join(BASE_DIR, '../../..')

_ENV_VAR = 'VAR_PATH'

SECRET_KEY = os.getenv('SECRET_KEY', '-05sgp9!deq=q1nltm@^^2cc+v29i(tyybv3v2t77qi66czazj')

VAR_PATH = os.getenv(_ENV_VAR, os.path.join(SRC_DIR, 'owl/src/var'))

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')

LANGUAGE_CODE = 'ru'

TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    f'{BASE_DIR}/locale',
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(VAR_PATH, 'static'))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(VAR_PATH, 'media'))

# Создаёт папки `media` & `var` при их отсутствии:
for path in (VAR_PATH, MEDIA_ROOT):
    if not os.path.exists(path):
        os.mkdir(path)

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(BASE_DIR, 'static')),
)
