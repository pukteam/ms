# SECURITY WARNING: keep the secret key used in production secret!
from ast import literal_eval
import os
from MoneySystem.project_settings.base import BASE_DIR, PROJECT_ROOT

SECRET_KEY = 'zjwslz((l79v(^22$ts=g4+)j^r$+uz0(uxs4ht4!g8ipfmz1s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(literal_eval(os.environ.get("MS_DEBUG", "True")))
LOCAL = bool(literal_eval(os.environ.get("MS_LOCAL", "False")))
PROD = bool(literal_eval(os.environ.get("MS_PROD", "False")))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'whitenoise',
    'import_export',

    'representation',
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

    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'MoneySystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'MoneySystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, '../staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, '../static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

ugettext = lambda s: s

LANGUAGES = (
    ('ru', ugettext(u'Russian')),
    ('en', ugettext(u'English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
