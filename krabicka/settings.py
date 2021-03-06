"""
Django settings for krabicka project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import ldap

from django_auth_ldap.config import LDAPSearch, PosixGroupType

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l%(m6wmw=ac1(8(k7bwvtt&)8^+gc2wya7du*ws%(l$*=f9=3p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'krabicka.apps.KrabickaConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'oidc_provider',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'oidc_provider.middleware.SessionManagementMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'krabicka.urls'

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

AUTHENTICATION_BACKENDS = [
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]

WSGI_APPLICATION = 'krabicka.wsgi.application'


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

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

OIDC_SESSION_MANAGEMENT_ENABLE = True

CORS_ORIGIN_ALLOW_ALL = True
OIDC_LOGIN_URL = '/accounts/login/'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

AUTH_LDAP_SERVER_URI = "ldap://ldap.forumsys.com:389"
AUTH_LDAP_BIND_DN = "cn=read-only-admin,dc=example,dc=com"
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,dc=example,dc=com"
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_BIND_PASSWORD = "password"
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}
# # Set up the basic group parameters.
# AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
#     "ou=mathematicians,dc=example,dc=com", ldap.SCOPE_SUBTREE,
# )
# AUTH_LDAP_GROUP_TYPE = PosixGroupType
# AUTH_LDAP_DENY_GROUP = "ou=scientists,dc=example,dc=com"
# AUTH_LDAP_MIRROR_GROUPS = True
# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_staff": "ou=mathematicians,dc=example,dc=com",
# }
