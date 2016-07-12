"""
Django settings for {{ cookiecutter.project_name }} project.
"""

import os
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = '7x=ion&zd9%_hqv0)zc^rh6e#p$jw(8m#xqvt_viqb#fqv(n@+'
DEBUG = False
SITE_ID = 3

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    '{{cookiecutter.project_name}}.core',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'compressor',
    'django_tables2',
    'django_filters',
    'django_extensions',
    'reversion',
    'widget_tweaks',
]

MIDDLEWARE_CLASSES = [
    'reversion.middleware.RevisionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{cookiecutter.project_name}}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                '{{cookiecutter.project_name}}.core.context_processors.default_cp',
            ],
            'loaders': [
            ('django.template.loaders.cached.Loader', [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]),
        ],
        },
    },
]

WSGI_APPLICATION = '{{cookiecutter.project_name}}.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    }, {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }, {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    }, {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    }
]

LANGUAGE_CODE = 'el'
TIME_ZONE = 'Europe/Athens'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = '/home/serafeim/{{cookiecutter.project_name}}/static'
STATIC_URL = '/static_{{cookiecutter.project_name}}/'
MEDIA_URL = '/media_{{cookiecutter.project_name}}/'
MEDIA_ROOT = '/home/serafeim/{{cookiecutter.project_name}}/media'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGIN_URL = '/login/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': '{{cookiecutter.project_name}}',
    }
}
CACHE_MIDDLEWARE_KEY_PREFIX = '{{cookiecutter.project_name}}'
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# SECURITY OPTIONS
SECURE_HSTS_SECONDS = 0
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SESSION_COOKIE_SECURE = True # Careful this allows session to work only on HTTPS on production
CSRF_COOKIE_SECURE = True # Careful this allows CSRF to work only on HTTPS on production
CSRF_COOKIE_HTTPONLY = True

ADMINS = MANAGERS = [('{{cookiecutter.full_name}}', '{{cookiecutter.email}}'), ]

# Default for django-filter
FILTERS_HELP_TEXT_EXCLUDE = True
FILTERS_HELP_TEXT_FILTER = False

# EMAIL cfg
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.hcg.gr'
MAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@hcg.gr'
SERVER_EMAIL = 'noreply@hcg.gr'
EMAIL_HOST_PASSWORD = '' # Configure me in local.py
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@hcg.gr'

from .ldap_conf import *
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    '{{cookiecutter.project_name}}.core.auth.NoLoginModelBackend',
)