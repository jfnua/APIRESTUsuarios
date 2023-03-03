
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Application definition
BASE_APPS = [
    'material',
    'material.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
  "apps.users",
]

THIRD_APPS = [
  "rest_framework",
  "simple_history",
  "corsheaders",
  "drf_yasg",
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mascore.urls'

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

WSGI_APPLICATION = 'mascore.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Hermosillo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
  BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / 'staticfiles/'

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#modelo a usar para la autentificacion
AUTH_USER_MODEL = "users.User"

#CONFIGURACION PÄRA SWAGGER
SWAGGER_SETTINGS = {
  "DOC_EXPANSION": "none",
}


#Config Template material admin
MATERIAL_ADMIN_SITE = {
    'FAVICON':  'admin/img/favicon.png',  # Admin site favicon (path to static should be specified)
    'HEADER':  _('Administración Mascore'),  # Admin site header
    'TITLE':  _('Mascore'),  # Admin site title
    'PROFILE_PICTURE':  "path/to/image",  # Admin site profile picture (path to static should be specified), or if model has a image field set the image for that user
    'PROFILE_BG':  '',  # Admin site profile background (path to static should be specified)
    'MAIN_BG_COLOR':  '#181848',  # Admin site main color, css color should be specified
    'MAIN_HOVER_COLOR':  '#7890a8',  # Admin site main hover color, css color should be specified
    'SHOW_THEMES':  False,  #  Show default admin themes button
    'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': True,  # Hide side navbar by default
    'SHOW_COUNTS': True, # Show instances counts for each model
    'LOGIN_LOGO':  'admin/img/logo.svg',  # Admin site logo on login page (path to static should be specified)
    'LOGOUT_BG':  'admin/img/login_bg.jpg',  # Admin site background on login/logout pages (path to static should be specified)
}
"""
    #Otros configuraciones del template material admin
    'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
        'sites': 'send',
    },
    'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
        'site': 'contact_mail',
    }
"""