from .base import *

# These should be imprted from from base.py but I'll redefine them for clarity
DEBUG = False
SITE_ID = 1

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)



try:
    from .local import *
except ImportError:
    pass
