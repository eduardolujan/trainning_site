"""Base settings shared by all environments"""
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *   # pylint: disable=W0614,W0401

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#v+99+abve=)d4lmuq7h2qe-yh8$voqii5*9+uu9a(t670+$bf'


#==============================================================================
# Installed Apps
#==============================================================================


INSTALLED_APPS = (
    'trainning_site.apps.trainning',

    #'south',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

import os
import sys
import trainning_site as project_module

PROJECT_DIR , PROJECT_MODULE_NAME = os.path.split(os.path.dirname(os.path.realpath(project_module.__file__)))
if not PROJECT_DIR in sys.path:
  sys.path.insert(0, PROJECT_DIR)

PYTHON_BIN = os.path.dirname(sys.executable)
ve_path = os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR)))
# Assume that the presence of 'activate_this.py' in the python bin/
# directory means that we're running in a virtual environment.
if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
    # We're running with a virtualenv python executable.
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
elif ve_path and os.path.exists(os.path.join(ve_path, 'bin',
        'activate_this.py')):
    # We're running in [virtualenv_root]/src/[project_name].
    VAR_ROOT = os.path.join(ve_path, 'var')
else:
    # Set the variable root to a path in the project which is
    # ignored by the repository.
    VAR_ROOT = os.path.join(PROJECT_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)


SQLITE_DB_ROOT = os.path.join(PROJECT_DIR, 'db')
if not os.path.exists(SQLITE_DB_ROOT):
    os.mkdir(SQLITE_DB_ROOT)


# Add the 'wis' dir to the python path
MODULE_DIR = os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME)
if not MODULE_DIR in sys.path:
    sys.path.insert(1, MODULE_DIR)

# Add the 'apps' dir to the python path
APPS_DIR = os.path.join(MODULE_DIR, 'apps')
if not APPS_DIR in sys.path:
    sys.path.insert(2, APPS_DIR)

# Add the 'lib' dir to the python path
LIB_DIR = os.path.join(MODULE_DIR, 'lib')
if not LIB_DIR in sys.path:
    sys.path.insert(3, LIB_DIR)

UPLOADS = os.path.join(PROJECT_DIR, "uploads")
if not LIB_DIR in sys.path:
    sys.path.insert(3, UPLOADS)



#sys.path.insert(1, PROJECT_DIR) 
#sys.path.insert(2, os.path.join(PROJECT_DIR, "apps")) 
#sys.path.insert(3, os.path.join(PROJECT_DIR, "lib")) 
#sys.path.insert(3, os.path.join(PROJECT_DIR, "uploads")) 




#==============================================================================
# Project URLS and media settings
#==============================================================================

ROOT_URLCONF = 'trainning_site.urls'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')


STATICFILES_DIRS = (
    os.path.join(MODULE_DIR, 'static'),
)






#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(MODULE_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',

)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(MODULE_DIR, 'templates'),],
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

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS += (
)


AUTH_USER_MODEL = 'trainning.SystemUser'

#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================
