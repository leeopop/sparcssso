"""
Django settings for sparcssso project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'keys/django_secret')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['sso.sparcs.org', '143.248.234.129']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.account',
    'apps.oauth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'sparcssso.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sparcssso.wsgi.application'

LOGIN_URL = '/account/login/'

LOGOUT_URL = '/account/logout/'


# Facebook, Twitter, KAIST API Key

with open(os.path.join(BASE_DIR, 'keys/fb_app_id')) as f:
    FACEBOOK_APP_ID = f.read().strip()

with open(os.path.join(BASE_DIR, 'keys/fb_app_secret')) as f:
    FACEBOOK_APP_SECRET = f.read().strip()

with open(os.path.join(BASE_DIR, 'keys/tw_app_id')) as f:
    TWITTER_APP_ID = f.read().strip()

with open(os.path.join(BASE_DIR, 'keys/tw_app_secret')) as f:
    TWITTER_APP_SECRET = f.read().strip()

with open(os.path.join(BASE_DIR, 'keys/kaist_app_secret')) as f:
    KAIST_APP_SECRET = f.read().strip()

with open(os.path.join(BASE_DIR, 'keys/kaist_app_admin_id')) as f:
    KAIST_APP_ADMIN_ID = f.read().strip()

with open(os.path.join(BASE_DIR, 'keys/kaist_app_admin_pw')) as f:
    KAIST_APP_ADMIN_PW = f.read().strip()


# E-mail settings
EMAIL_HOST = 'localhost'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sso',
        'USER': 'sso',
        'PASSWORD': 'DUMMY',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

with open(os.path.join(BASE_DIR, 'keys/db_pw')) as f:
    DATABASES['default']['PASSWORD'] = f.read().strip()


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Admins & Logging
ADMINS = (('SSO SYSOP', 'sso@sparcs.org'),)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'std': {
            'format': '%(levelno)s/%(asctime)s (%(ip)s, %(username)s) %(name)s - %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'apps.logger.FileHandler',
            'filename': '/data/log/sso/info.log',
            'maxBytes': 30 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'std',
        },
        'mail': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail'],
            'level': 'ERROR',
        },
        'sso': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}
