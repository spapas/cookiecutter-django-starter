from .base import *

DEBUG = True
SITE_ID = 2

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)


try:
    from .local import *
except ImportError:
    pass
