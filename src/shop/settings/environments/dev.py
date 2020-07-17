"""Dev настройки приложения."""

import logging

from corsheaders.defaults import default_headers, default_methods

from shop.settings.environments.base import *  # @UnusedWildImport


USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ('*',)

CORS_ALLOW_CREDENTIALS = False

CORS_ALLOW_HEADERS = list(default_headers)

CORS_ALLOW_METHODS = list(default_methods)


INSTALLED_APPS = INSTALLED_APPS + (
    'nplusone.ext.django',
)

MIDDLEWARE = MIDDLEWARE + (
    'nplusone.ext.django.NPlusOneMiddleware',
)


NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN

DEBUG = os.getenv('DEBUG', True)
