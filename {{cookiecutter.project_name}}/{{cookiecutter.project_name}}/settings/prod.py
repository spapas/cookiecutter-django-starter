from .base import *

# These should be imprted from from base.py but I'll redefine them for clarity
DEBUG = False
SITE_ID = 1

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


try:
    from .local import *
except ImportError:
    pass
