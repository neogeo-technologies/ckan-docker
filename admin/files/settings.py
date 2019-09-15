"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
#TODO
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a_generer'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

#TODO
DOMAIN_NAME = '127.0.0.1:8181'
#DOMAIN_NAME = 'https://admin.dev.idgo.neogeo.fr'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'taggit',
    'bootstrap3',
    'mama_cas',
    'idgo_admin'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#TODO
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'idgo_admin',
        'USER': 'idgo_admin',
        'PASSWORD': 'password',
        'HOST':'db_admin',
        'PORT':'5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-passwordword-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.passwordword_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.passwordword_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.passwordword_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.passwordword_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'FR-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/var/www/html/static/'

MEDIA_ROOT = '/var/www/html/media/'

MEDIA_URL = '/media/'

CKAN_URL = 'http://ckan'
CKAN_API_KEY = 'CKAN_API_KEY_TO_REPLACE'
CKAN_TIMEOUT = 36000


GEONETWORK_URL = 'https://geonetwork.dev.idgo.neogeo.fr/geonetwork/'
GEONETWORK_LOGIN = 'admin'
GEONETWORK_PASSWORD = 'admin'

READTHEDOC_URL = 'http://datasud.readthedocs.io/fr/latest/producteurs.html#comment-renseigner-les-metadonnees-sur-datasud'
READTHEDOC_URL_INSPIRE = 'http://datasud.readthedocs.io/fr/latest/producteurs.html#comment-renseigner-les-metadonnees-inspire-sur-datasud'

# EMAIL config
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_HOST = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = 'password'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'admin'

# Other stuffs

LOGIN_URL = 'idgo_admin:signIn'
#TODO
MAMA_CAS_SERVICES = [
        { # CKAN
            'SERVICE': '^http://localhost:8080/',
            'CALLBACKS': [
                'mama_cas.callbacks.user_name_attributes',
                'mama_cas.callbacks.user_model_attributes'
                ],
            'LOGOUT_ALLOW': True,
            'LOGOUT_URL': 'https://localhost:8080/cas/logout'
        },
]
