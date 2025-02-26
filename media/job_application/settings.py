import os
from pathlib import Path
from dotenv import load_dotenv
import secrets

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Генерируем случайный ключ если не задан в .env
SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_urlsafe(50))

# В продакшене DEBUG должен быть False
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Ограничиваем список разрешенных хостов
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'django_celery_beat',
    'drf_yasg',
    'ckeditor',
    'ckeditor_uploader',
    'django_ratelimit', # Добавляем rate limiting
    'axes', # Защита от брутфорса

    #apps
    'main',
    'user', 
    'blockchain',
    'home',
    'data',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware', # Защита от брутфорса
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

# Улучшенные настройки базы данных с таймаутами и SSL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
        'OPTIONS': {
            'sslmode': 'require',
            'connect_timeout': 3,
        }
    }
}

# Усиленные валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 14,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# CORS настройки с разрешением для всех источников
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET', 
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Безопасные настройки для CKEditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'height': 300,
        'width': '100%',
        'removePlugins': 'flash,iframe,embed,object',
    },
}

# Локализация
LANGUAGES = [
    ('ru', 'Русский'),
    ('en', 'English'), 
    ('ky', 'Кыргызча'),
]
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_TZ = True

# Безопасные настройки для загрузки файлов
CKEDITOR_UPLOAD_PATH = os.getenv('CKEDITOR_UPLOAD_PATH', 'uploads/')
CKEDITOR_BASEPATH = os.getenv('CKEDITOR_BASEPATH', '/static/ckeditor/ckeditor/')
CKEDITOR_IMAGE_BACKEND = os.getenv('CKEDITOR_IMAGE_BACKEND', 'pillow')
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True

# Настройки Celery с улучшенной безопасностью
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = os.getenv('CELERY_TIMEZONE', 'UTC')
CELERY_SECURITY_KEY = os.getenv('CELERY_SECURITY_KEY', secrets.token_hex(32))
CELERY_TASK_ACKS_LATE = True
CELERY_WORKER_MAX_TASKS_PER_CHILD = 1000

AUTH_USER_MODEL = os.getenv('AUTH_USER_MODEL', 'user.User')

# Безопасные настройки для статических и медиа файлов
STATIC_URL = os.getenv('STATIC_URL', 'static/')
STATIC_ROOT = os.path.join(BASE_DIR, os.getenv('STATIC_ROOT', '/static/').lstrip('/'))
MEDIA_URL = os.getenv('MEDIA_URL', '/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv('MEDIA_ROOT', 'media/').lstrip('/'))
VERIFICATION_DIR = os.path.join(MEDIA_ROOT, 'verification/txt')
os.makedirs(VERIFICATION_DIR, exist_ok=True)
os.chmod(VERIFICATION_DIR, 0o750)

# Настройки безопасности email с проверкой конфигурации
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
if not all([EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD]):
    raise ValueError("Email settings must be configured")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Улучшенные настройки кэширования
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
            'RETRY_ON_TIMEOUT': True,
            'MAX_CONNECTIONS': 1000,
            'COMPRESSOR': 'django_redis.compressors.zlib.ZlibCompressor',
        }
    }
}

# Расширенное логирование безопасности
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'verbose',
        },
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/security.log'),
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security'],
            'level': 'INFO',
            'propagate': True,
        },
        'axes': {
            'handlers': ['security'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

# Создаем директорию для логов с правильными правами
os.makedirs(os.path.join(BASE_DIR, 'logs'), exist_ok=True)
os.chmod(os.path.join(BASE_DIR, 'logs'), 0o750)

# Настройки для защиты от брутфорса
AXES_FAILURE_LIMIT = 5  # Количество попыток до блокировки
AXES_COOLOFF_TIME = 1  # Время блокировки в часах
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True  # Блокировка по комбинации юзер+IP

# Rate limiting
RATELIMIT_ENABLE = True
RATELIMIT_USE_CACHE = 'default'
RATELIMIT_VIEW = 'ratelimit.views.limited'
