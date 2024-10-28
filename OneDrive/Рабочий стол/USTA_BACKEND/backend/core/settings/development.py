import os
from pathlib import Path
from decouple import config
# cuser/middleware.py
from compat import User

# Затем в коде, где используется User, замените:
# user = User()
# на:
user = User()

# Основной путь проекта
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print("POSTGRES_DB:", config('POSTGRES_DB'))
print("POSTGRES_USER:", config('POSTGRES_USER'))
print("POSTGRES_PASSWORD:", config('POSTGRES_PASSWORD'))
print("POSTGRES_HOST:", config('POSTGRES_HOST'))
print("POSTGRES_PORT:", config('POSTGRES_PORT'))


# Режим отладки
DEBUG = True

# Конфигурация базы данных (SQLite для разработки)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("POSTGRES_DB"),
        'USER': config("POSTGRES_USER"),
        'PASSWORD': config("POSTGRES_PASSWORD"),
        'HOST': config("POSTGRES_HOST"),
        'PORT': config("POSTGRES_PORT"),
    }
}


# Статические файлы и медиа
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
STATICFILES_DIRS = [BASE_DIR / "media/static"]
