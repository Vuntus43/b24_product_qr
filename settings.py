import os

APP_SETTINGS = None

ADMINS = (
    ('img', 'img@it-solution.ru'),
)

BASE_DOMAIN = ''  # заполним позже, когда будет домен
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(__file__).replace('\\','/')

# В деве можно оставить любой ключ, в проде вынести в ENV
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-only-change-me')

DEBUG = True  # как в is_demo-подходе, для старта включим
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    # 'integration_utils.bitrix24',              # включим после добавления сабмодуля
    # 'integration_utils.its_utils.app_gitpull', # включим после добавления сабмодуля

    'products_qr',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',  # как в is_demo, не используем
]

ROOT_URLCONF = 'urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

WSGI_APPLICATION = 'wsgi.application'

# PostgreSQL через psycopg (современный драйвер). Вы установили БД b24_qr.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # современное имя бэкенда
        'NAME': 'b24_qr',
        'USER': 'postgres',
        'PASSWORD': 'Vanek2004!',   # набери заново
        'HOST': '127.0.0.1',        # предпочтительнее, чем 'localhost' на Windows
        'PORT': '5432',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
ENTRY_FILE_UPLOADING_FOLDER = os.path.join(MEDIA_ROOT, 'uploaded_entrie_files')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]

# Логи (как в is_demo) — заглушка, чтобы не падало, если integration_utils ещё не подключён
try:
    from integration_utils.its_utils.mute_logger import MuteLogger  # type: ignore
    ilogger = MuteLogger()
except Exception:
    ilogger = None  # подключим позже

# local settings (как в is_demo)
try:
    from local_settings import *  # noqa
except ImportError:
    from warnings import warn
    warn('create local_settings.py')

# APP_SETTINGS: подхватим из local_settings, иначе простая заглушка до подключения integration_utils
if not APP_SETTINGS:
    class _LocalSettingsFallback:
        app_domain = ''
        app_name = 'b24_product_qr'
        salt = ''
        secret_key = ''
        application_index_path = '/'
    APP_SETTINGS = _LocalSettingsFallback()

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Для работы в iframe Битрикс24 (ваш чек-лист)
SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = False  # включим True, когда будет https
CSRF_COOKIE_SECURE = False
