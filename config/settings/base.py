from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent.parent


# ==========================================
# CORE SETTINGS
# ==========================================

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []


# ==========================================
# DJANGO APPS
# ==========================================

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# ==========================================
# THIRD PARTY APPS
# ==========================================

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
]


# ==========================================
# LOCAL APPS
# ==========================================

LOCAL_APPS = [
    'apps.authentication',
    # 'apps.posts',
]


INSTALLED_APPS = (
    DJANGO_APPS
    + THIRD_PARTY_APPS
    + LOCAL_APPS
)


# ==========================================
# MIDDLEWARE
# ==========================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==========================================
# URLS
# ==========================================

ROOT_URLCONF = 'config.urls'


# ==========================================
# TEMPLATES
# ==========================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ==========================================
# WSGI
# ==========================================

WSGI_APPLICATION = 'config.wsgi.application'


# ==========================================
# DATABASE
# ==========================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}


# ==========================================
# PASSWORD VALIDATORS
# ==========================================

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


# ==========================================
# INTERNATIONALIZATION
# ==========================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True


# ==========================================
# STATIC FILES
# ==========================================

STATIC_URL = 'static/'


# ==========================================
# MEDIA FILES
# ==========================================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# ==========================================
# DEFAULT PRIMARY KEY
# ==========================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==========================================
# CUSTOM USER MODEL
# ==========================================

AUTH_USER_MODEL = 'authentication.User'


# ==========================================
# DJANGO REST FRAMEWORK
# ==========================================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'EXCEPTION_HANDLER': (
        'apps.core.exceptions.custom_exception_handler'
    )
}


# ==========================================
# JWT SETTINGS
# ==========================================

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),

    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,

    'UPDATE_LAST_LOGIN': True,
}