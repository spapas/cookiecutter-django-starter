from .base import *

DEBUG = True
SITE_ID = 2

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

CSRF_COOKIE_SECURE = False # Override CSRF to work also with http
SESSION_COOKIE_SECURE = False # Override session to work also with http

try:
    from .local import *
except ImportError:
    pass
