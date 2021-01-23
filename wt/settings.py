"""
Django settings for wt project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url
#import dotenv
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fla9rqv@n4b$f)qk#z*wowt3va&&oj8&#0rjf5p#g25y0pz567'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'django_extensions',
    # 'debug_toolbar',

    'social_django',
    
    'blog.apps.BlogConfig',
    'members',
    'ckeditor',
    'shop.apps.ShopConfig',

    #'django_email_verification',
    #"phone_verify",
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'wt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here

            ],
        },
    },
]

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link'] # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       # add this
  'fields': 'id, name, email, picture.type(large), link'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 # add this
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]



WSGI_APPLICATION = 'wt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

import psycopg2.extensions



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wt',
        'USER':'postgres',
        'PASSWORD':'koko2009.',
        'HOST':'localhost',
    }
}



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

MEDIA_URL ='/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 

LOGIN_REDIRECT_URL='home'
LOGOUT_REDIRECT_URL='home'

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'

SOCIAL_AUTH_GITHUB_KEY = '5df155baf1c4a7b2758a'
SOCIAL_AUTH_GITHUB_SECRET = '7d86f2d9570ba11889930d5e7f4dc2ee04161370'

SOCIAL_AUTH_FACEBOOK_KEY = '3200748226640329'
SOCIAL_AUTH_FACEBOOK_SECRET = '8f03ff93c2b53ddc3e23eacf8aae8ef4'


SOCIAL_AUTH_INSTAGRAM_KEY = '306801273808727' #Client ID
SOCIAL_AUTH_INSTAGRAM_SECRET = '1e46bad679a73e831a7eb3a9a769825e'#Client SECRET
SOCIAL_AUTH_INSTAGRAM_EXTRA_DATA = [('user', 'user'),
]



#STATIC_ROOT =os.path.join(BASE_DIRS,'assets')

#MEDIA_URL='/media/'
#MEDIA_ROOT =os.path.join(BASE_DIRS,'media')


#INTERNAL_IPS=['127.0.0.1']

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',
    
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'home'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False



# EMAIL_ACTIVE_FIELD = 'is_active'
# EMAIL_SERVER = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_ADDRESS = 'lovjes4@gmail.com'
# EMAIL_FROM_ADDRESS = 'noreply@aliasaddress.com'
# EMAIL_PASSWORD = 'koko2009.' # os.environ['password_key'] suggested
# EMAIL_MAIL_SUBJECT = 'Confirm your email'
# EMAIL_MAIL_HTML = 'mail_body.html'
# EMAIL_MAIL_PLAIN = 'mail_body.txt'
# EMAIL_PAGE_TEMPLATE = 'confirm_template.html'
# EMAIL_PAGE_DOMAIN = 'http://mydomain.com/'





PHONE_VERIFICATION = {
    "BACKEND": "phone_verify.backends.twilio.TwilioBackend",
    "OPTIONS": {
        "SID": "fake",
        "SECRET": "fake",
        "FROM": "+14755292729",
        "SANDBOX_TOKEN": "123456",
    },
    "TOKEN_LENGTH": 6,
    "MESSAGE": "Welcome to {app}! Please use security code {security_code} to proceed.",
    "APP_NAME": "Phone Verify",
    "SECURITY_CODE_EXPIRATION_TIME": 3600,  # In seconds only
    "VERIFY_SECURITY_CODE_ONLY_ONCE": False,  # If False, then a security code can be used multiple times for verification
}
django_heroku.settings(locals())
