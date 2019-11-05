"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from django.core.exceptions import ImproperlyConfigured
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1lt-@_35_-s(x)bvgkq8ltg73!c-qa=p6k_@5o$)dg5gh68tz%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1', '535a68f3.ngrok.io']


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'images.apps.ImagesConfig',
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

ROOT_URLCONF = 'bookmarks.urls'

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

WSGI_APPLICATION = 'bookmarks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# For serving media files uploaded by users with the development server (p. 125)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Add email authentication in additional to default method (p. 134)
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
]

# Use environment variables for loading secrets
# Code snippet based on post from Daniel Roy Greenfeld
# https://www.pydanny.com/using-executable-code-outside-version-control.html


def get_env_var(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f'Set the {var_name} environment variable'
        raise ImproperlyConfigured(error_msg)


# Obtain settings for Bookmarks Facebook app at URL below:
# https://developers.facebook.com/apps/2637851352962069/settings/basic/
# Facebook App ID
#SOCIAL_AUTH_FACEBOOK_KEY = get_env_var('SOCIAL_AUTH_FACEBOOK_KEY')
# Facebook App Secret
#SOCIAL_AUTH_FACEBOOK_SECRET = get_env_var('SOCIAL_AUTH_FACEBOOK_SECRET')
#SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Obtain settings for Bookmarks-JDB Twitter app at URL below:
# https://developer.twitter.com/en/apps/16904022
# Twitter Consumer Key
#SOCIAL_AUTH_TWITTER_KEY = get_env_var('SOCIAL_AUTH_TWITTER_KEY')
# Twitter Consumer Secret
#SOCIAL_AUTH_TWITTER_SECRET = get_env_var('SOCIAL_AUTH_TWITTER_SECRET')

# Obtain settings for Bookmarks Google+ app at URL below:
# https://console.developers.google.com/apis/dashboard?project=bookmarks-257319
# Google Consumer Key
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_env_var('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
# Google Consumer Secret
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_env_var('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
