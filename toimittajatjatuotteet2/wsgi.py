"""
WSGI config for toimittajatjatuotteet2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
settings_module = "suppliers.production" if 'WEBSITE_HOSTNAME' in os.environ else 'suppliers.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toimittajatjatuotteet2.settings')


'''
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suppliers.settings')
'''


application = get_wsgi_application()
