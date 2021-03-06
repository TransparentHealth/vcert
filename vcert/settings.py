# Django settings for vcert project.

import os
from django.utils.translation import ugettext_lazy as _
from django.conf import global_settings
from django.contrib.messages import constants as messages

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('You', 'you@example.com'),
)

MANAGERS = ADMINS

BASE_DIR = os.path.join( os.path.dirname( __file__ ), '..' )
MANAGERS = ADMINS


DBPATH=os.path.join(BASE_DIR, 'db/db.db')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DBPATH,                   # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False


#Authentication
AUTH_PROFILE_MODULE = 'accounts.userprofile'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'sitestatic'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ej)&g6=#-jwzbdngm_)c5wz)(j$6c5toled%0@0pljih3(3w=j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'vcert.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'vcert.wsgi.application'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'apps/home/templates'),
    
    # This should always be the last in the list because it is our
    # fallback default.
    os.path.join(BASE_DIR, 'templates'), 
)


LOCALE_PATHS = (
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'locale'),
)



INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    #This project
    'apps.accounts',
    'apps.certificates',
    'apps.home',
    #3rd party
    'direct',
    'widget_tweaks',
    'django_extensions',
    'bootstrapform',
    'mptt',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


MESSAGE_TAGS ={ messages.DEBUG: 'info',
                messages.INFO: 'info',
                messages.SUCCESS: 'success',
                messages.WARNING: 'warning',
                messages.ERROR: 'danger',}


# Email Settings -----------------------------------------------------------

EMAIL_HOST_USER = 'vcert@example.com'
HOSTNAME_URL = 'http://127.0.0.1:8000'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

# Default S3 bucket for file upload utility.
AWS_BUCKET =''

# Twilio is not yet supported, but these are added for future multi-factor
# authentication support requiring a mobile phone for login.


#Org  and CA Settings -----------------------------------------------------
# Send outbound emails such as #verification notification and more
SEND_CA_EMAIL       = False
MIN_PASSWORD_LEN = 8
SIGNUP_TIMEOUT_DAYS = 3
PASSWORD_RESET_TIMEOUT_HOURS = 24
REQUEST_ACCOUNT_URL = "http://example.com/request-account"
ORGANIZATION_NAME = "Sample-CA"
CA_COMMON_NAME = "ca.example.com"
LOCATION_NAME = "Anywhere, USA"
GLOBAL_TITLE = "caconsole.example.com"
CA_VERIFIER_EMAIL = "verifier@example.com"
CA_HOSTNAME = "localhost:8000/static"
CA_URL = 'http://%s/' % (CA_HOSTNAME)

#Valid options are "LOCAL" only. S3" is not supported at this time.
CA_PUBLICATION_OPTIONS = ("LOCAL", ) #

ACCOUNT_REQUEST_TEXT = "Contact example@example.com for a code."

# Not recommended to adjust this part

#CA Directory structure -------------------------------------------
CA_BASE_DIR              = "/opt/ca/"
CA_CONF_DIR              = os.path.join( CA_BASE_DIR, 'conf/' )
CA_MAIN_CONF             = os.path.join( CA_CONF_DIR , 'root.cnf')
CA_MAIN_SERIAL           = os.path.join( CA_CONF_DIR , 'serial')
CA_PRIVATE_DIR           = os.path.join( CA_BASE_DIR, 'private/' )
CA_PUBLIC_DIR            = os.path.join( CA_BASE_DIR, 'public/' )
CA_SIGNED_DIR            = os.path.join( CA_BASE_DIR, 'signed-keys/' )
CA_COMPLETED_DIR         = os.path.join( CA_BASE_DIR, 'completed/' )
CA_INPROCESS_DIR         = os.path.join( CA_BASE_DIR, 'inprocess/' )
CA_INPROCESS_ANCHOR_DIR  = os.path.join( CA_INPROCESS_DIR, 'anchors/' )
CA_INPROCESS_ENDPOINTS_DIR  = os.path.join( CA_INPROCESS_DIR, 'endpoints/' )
CA_PUBLIC_CERT_NAME      = "%s.pem" % (CA_COMMON_NAME)
CA_PUBLIC_CRL_NAME       = "%s.crl" % (CA_COMMON_NAME)
CA_PUBLIC_AIA_NAME       = "%s.der" % (CA_COMMON_NAME)


#Published Local Filesystem
#LOCAL_CRL_PATH           = os.path.join(BASE_DIR, 'sitestatic', 'crl')
LOCAL_ROOT_CRL_PATH      = os.path.join(BASE_DIR, 'sitestatic', 'crl/', CA_PUBLIC_CRL_NAME )
LOCAL_ROOT_AIA_PATH      = os.path.join(BASE_DIR, 'sitestatic', 'aia/', CA_PUBLIC_CERT_NAME )
LOCAL_CRL_PATH           = os.path.join(BASE_DIR, 'sitestatic', 'crl')
LOCAL_AIA_PATH           = os.path.join(BASE_DIR, 'sitestatic', 'aia')
LOCAL_PUBLIC_PATH        = os.path.join(BASE_DIR, 'sitestatic', 'public')
LOCAL_PRIVATE_PATH       = os.path.join(BASE_DIR, 'sitestatic', 'private')
LOCAL_RCSP_PATH          = os.path.join(BASE_DIR, 'sitestatic', 'rcsp')
LOCAL_RCSPSHA1_PATH      = os.path.join(BASE_DIR, 'sitestatic', 'rcsp-sha1')
LOCAL_X5C_PATH           = os.path.join(BASE_DIR, 'sitestatic', 'x5c')


#URLS for certs. aia, crl, etc.-----------------------------------------------
CRL_FILENAME               = os.path.join(CA_COMMON_NAME , ".crl")
CRL_URL_PREFIX              = '%s%s/'    % (CA_URL, "crl")
CA_ROOT_CRL_URL             = '%s%s.crl' % (CRL_URL_PREFIX, CA_COMMON_NAME)
CA_ROOT_AIA_URL             = '%s%s.der' % (CRL_URL_PREFIX, CA_COMMON_NAME)
AIA_URL_PREFIX              = '%s%s/'    % (CA_URL, "aia")
PRIVATE_URL_PREFIX          = '%s%s/'    % (CA_URL, "private")
PUBLIC_URL_PREFIX           = '%s%s/'    % (CA_URL, "public")
RCSP_URL_PREFIX             = '%s%s/'    % (CA_URL, "rcsp")
RCSPSHA1_URL_PREFIX         = '%s%s/'    % (CA_URL, "rcsp-sha1")
X5C_URL_PREFIX              = '%s%s/'    % (CA_URL, "x5c")
CHAIN_URL_PREFIX            = '%s%s/'    % (CA_URL, "chain")

# The S3 bucket for the certificate revocation lists.  This "webserver" is
# used by all trust anchors.


#S3 Settings -------------------------------------
CRL_BUCKET          = "ca.example.com"
#A bucket for the X5C certificate chain
X5C_BUCKET          = "pubcerts.example.com"
#A bucket for public certs in pem, dir and x12 formats.
PUBCERT_BUCKET      = "pubcerts.example.com"
# A bucket for private certificates
PRIVCERT_BUCKET     = "privcerts.example.com"
# A bucket to contain a JSON representation of the certificate revocation status
RCSP_BUCKET         = "rcsp.example.com"
RCSPSHA1_BUCKET     = "rcspsha1.example.com"


TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + \
                ('apps.context_processors.global_title',
                 'apps.context_processors.ca_common_name',
                 'apps.context_processors.ca_url',
                 )

PRIVATE_PASSWORD = "changem3"

# To enable you local settings create or copy the example
# file found in ./config/settings_[EXAMPLE].py to the same
# directory as settings.py
try:
    from settings_local import *
except ImportError:
    pass
