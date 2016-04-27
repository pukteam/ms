from .django import *
from .local import *

if PROD and not LOCAL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  # django.db.backends.postgresql_psycopg2
            'NAME': os.environ["MS_DB_DEFAULT_NAME"],
            'USER': os.environ["MS_DB_DEFAULT_USER"],
            'PASSWORD': os.environ["MS_DB_DEFAULT_PASSWORD"],
            'HOST': os.environ["MS_DB_DEFAULT_HOST"],
            'PORT': os.environ["MS_DB_DEFAULT_PORT"],
        }
    }
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
