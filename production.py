import os
#import sys


# Configure the domain name using the enviroment variable 
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNANE' in os. environ else []


# Whitenoise configuration
MIDDLEWARE = [

    'Django.middleware.scurity.Securitymiddleware',
# add whitenoise middleware after the security middleware

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'Django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.Commonmiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessagesMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedmanifestStaticFilessStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#DBHOST is only the server name, not the full url

hostname = os.environ['DBHOST']

# Configure postgres database; the full username is username@servername
# which we construct using the dbhost value.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'HOST': hostname + ".postgres.database.azure.com"
        'USER': os.environ['DBUSER'] + "@" + hostname,
        'PASSWORD': os.environ['DBPASS']
    }
}