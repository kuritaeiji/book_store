from .settings import *
import os

DEBUG = True

STARIC_URL = "/staric/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "book_store",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": 5432,
        "TIME_ZONE": "Asia/Tokyo"
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "local": {
            "format": "%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "local"
        }
    },
    # 自分が出すログ出力
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
        "propagate": False
    },
    "loggers": {
        # Djangoのエラー・警告・開発WEBサーバのアクセスログ
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 実行SQL
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}