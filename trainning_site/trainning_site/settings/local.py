"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to trainning_site/settings/local.py. It should not be checked into
your code repository.

"""
from trainning_site.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('elujan', 'eduardo.lujan.net@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SQLITE_DB_ROOT, 'dev.db'),

    }
}

# ROOT_URLCONF = 'trainning_site.urls.local'
# WSGI_APPLICATION = 'trainning_site.wsgi.local.application'
