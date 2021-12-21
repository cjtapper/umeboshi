"""Minimal django settings to run manage.py test command"""

from celery import current_app

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": __name__,
    }
}

BROKER_BACKEND = "memory"


CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
current_app.conf.CELERY_ALWAYS_EAGER = True
current_app.conf.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

CELERY_EAGER_TRANSACTION = True

MIDDLEWARE_CLASSES = ()

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "umeboshi",
)

USE_TZ = True
SECRET_KEY = "django_tests_secret_key"
TIME_ZONE = "America/New_York"
LANGUAGE_CODE = "en-us"
ADMIN_MEDIA_PREFIX = "/static/admin/"
STATICFILES_DIRS = ()
