"""
Django settings for filminate project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^b5w0-ze1oz)9vyl(*(u8(3%=qwnzm_trabojze306+2y+4o#&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'accounts',
    'movies',
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'corsheaders',
    'django.contrib.sites',
    'allauth',
    'rest_auth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # allauth - google
    'allauth.socialaccount.providers.google',
    # allauth - naver
    # 'allauth.socialaccount.providers.naver',
    # allauth - kakao
    # 'allauth.socialaccount.providers.kakao',
]

SITE_ID = 2

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # 기본 인증 백엔드
    'allauth.account.auth_backends.AuthenticationBackend',  # allauth 인증 백엔드
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {  
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': '148338258564-qjotnbo2sd1bqaldt7k61jrvg1h1k428.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}


REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# REST-AUTH 회원가입 기본 Serailizer 재정의
REST_AUTH = {
 'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
 'USER_DETAILS_SERIALIZER': 'accounts.serializers.CustomUserDetailsSerializer',
 'LOGIN_SERIALIZER': 'accounts.serializers.CustomLoginSerializer',
}

# AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_ADAPTER = 'accounts.models.CustomAccountAdapter'

ACCOUNT_EMAIL_REQUIRED = True

LOGIN_REDIRECT_URL = 'http://localhost:8000/user/do_login/'
ACCOUNT_LOGOUT_REDIRECT_URL = 'http://localhost:5173/'
ACCOUNT_LOGOUT_ON_GET = True
# SOCIALACCOUNT_LOGIN_ON_GET = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# CORS_ALLOWED_ORIGINS = [
#     'http://127.0.0.1:5173',
#     'http://localhost:5173',
#     'http://127.0.0.1:8000',
#     'http://localhost:8000',
# ]
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
]

ROOT_URLCONF = 'filminate.urls'

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

WSGI_APPLICATION = 'filminate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'filminate',
        'USER': 'root',
        'PASSWORD': 'mysql123!',
        'HOST': 'localhost', # MySQL 호스트
        'PORT': '3306',      # MySQL 포트 (기본값은 3306)
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'
