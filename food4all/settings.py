"""
Django settings for food4all project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v98_#!h1tpoc#$qp9)b%8k-))dbo*r#pqj^wz@5uatj&-t$hte'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    # 'django_rest_passwordreset',
    'django_filters',
    'knox',
    'authentication',
    'foodwasteapp'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'food4all.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'frontend')],
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

WSGI_APPLICATION = 'food4all.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'foodappdb'
#     }
# }
'''
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'food4all-database',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
                'host': 'mongodb://food4all-server:JQ5FvncCkS7TyALJJDpef6ZBWkDAjJ2KnJERltUuQfJIJgqEnGMePrd5YiukWLficdoXBdndPV9VACDblsZu0g==@food4all-server.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@food4all-server@'
                # 'host': 'mongodb+srv://food4all-server:JQ5FvncCkS7TyALJJDpef6ZBWkDAjJ2KnJERltUuQfJIJgqEnGMePrd5YiukWLficdoXBdndPV9VACDblsZu0g==@food4all-server.mongo.cosmos.azure.com:10255/food4all-database?retryWrites=true&w=majority'

        }
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'food4all-database',
        'HOST': 'mongodb://food4all-server:JQ5FvncCkS7TyALJJDpef6ZBWkDAjJ2KnJERltUuQfJIJgqEnGMePrd5YiukWLficdoXBdndPV9VACDblsZu0g==@food4all-server.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@food4all-server@',
        # 'HOST': 'mongodb://food4all-server:JQ5FvncCkS7TyALJJDpef6ZBWkDAjJ2KnJERltUuQfJIJgqEnGMePrd5YiukWLficdoXBdndPV9VACDblsZu0g==@food4all-server.mongo.cosmos.azure.com:10255/food4all-database',
        'USER': 'food4all-server',
        'PASSWORD': 'JQ5FvncCkS7TyALJJDpef6ZBWkDAjJ2KnJERltUuQfJIJgqEnGMePrd5YiukWLficdoXBdndPV9VACDblsZu0g==',
    }
}

# 'host': 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority'
# 'mongodb+srv://username:password@HOSTNAME/DATABASE_NAME?authSource=admin&tls=true&tlsCAFile=<PATH_TO_CA_FILE>'
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend', "build",
                 "static"),  # update the STATICFILES_DIRS
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AUTH USER
AUTH_USER_MODEL = 'authentication.User'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000"
]

# GOOGLE_API_KEY = "AIzaSyDCUiR6W8hmQI3vEn_LkQebO2iIhKQJOfo"
# BASE_COUNTRY = "CA"
# google= AIzaSyDCUiR6W8hmQI3vEn_LkQebO2iIhKQJOfo
