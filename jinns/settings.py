"""
Django settings for jinns project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import datetime
from celery.schedules import crontab

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

try:
    os.makedirs(LOG_DIR)
except Exception:
    pass


ADMINS = (
    ('taojy', 'taojy123@163.com'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y-lf*oh7w(e^ptt^e+!_f+1l9xfgkxmb)fhhrwgt=c5*dn6p67'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'django_filters',

    'shop',
    'customer',
    'book',
    'mall',
    'order',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'jinns.middleware.Middleware',
]

ROOT_URLCONF = 'jinns.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'jinns.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jinns',
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'root'),
        'HOST': os.environ.get('MYSQL_HOST', '127.0.0.1'),
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = '/var/www/html/jinns_backend/media/'
STATIC_ROOT = '/var/www/html/jinns_backend/static/'

STATIC_URL = '/api/static/'
MEDIA_URL = '/api/media/'


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] "%(levelname)s %(module)s" %(message)s',
            'datefmt': '%d/%b/%Y %I:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'jinns.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'request_log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_DIR, 'requests.log'),
            'formatter': 'verbose'
        },
        'app_log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_DIR, 'apps.log'),
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins', 'console'],
            'level': 'INFO',
            'propagate': True
        },
        'apps': {
            'handlers': ['mail_admins', 'app_log_file'],
            'level': 'INFO',
            'propagate': True
        },
    }
}


# Email
SERVER_EMAIL = 'watchmen123456@163.com'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'watchmen123456'
EMAIL_HOST_PASSWORD = 'wm123456'
EMAIL_SUBJECT_PREFIX = '[jinns_backend] '


# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = [
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'cache-control',
    'x-http-method-override',
    'x-shop',
    'x-shop-id',
    'x-shop-domain',
    'x-bulk-operation',
    'x-frame-options',
]


# Rest framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'shop.authentication.ShopTokenAuthentication',
        'customer.authentication.CustomerTokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'shop.permissions.HasShop',
        # 'shop.permissions.IsShopOwnerOrReadOnly',
        # 'customer.permissions.IsCustomerOwnerOrReadOnly',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}


# qiniu
QINIU_ACCESS_KEY = 'QzBPrPDb8Vu1V0c2KV4ZL73exW4MkcjViESE9QKI'
QINIU_SECRET_KEY = 'pZnjwR_M_e-kTbLPi2EVKRSM4SdTDczs30Z_p49G'
QINIU_BUCKET_NAME = 'jinns'
QINIU_BUCKET_DOMAIN = 'p7iw1e96j.bkt.clouddn.com'
QINIU_SECURE_URL = False



# Celery
BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_SEND_TASK_ERROR_EMAILS = True
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600 * 24 * 100}
CELERYD_TASK_TIME_LIMIT = 60 * 30


# Celery Schedule
CELERYBEAT_SCHEDULE = {
    'daily_task': {
        'task': 'book.tasks.daily_task',
        'schedule': crontab(hour=1, minute=0),
        'args': (),
    },
}


# Local settings
try:
    LOCAL_SETTINGS  # @UndefinedVariable
except NameError:
    try:
        from .settings_local import *  # @UnusedWildImport
    except ImportError:
        pass



