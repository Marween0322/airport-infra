"""
WSGI config for hrmd project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

import sys

import site

from django.core.wsgi import get_wsgi_application

# Add the app’s directory to the PYTHONPATH

sys.path.append('C:/inetpub/www/hrmd')

sys.path.append('C:/inetpub/www/hrmd/hrmd')

os.environ['DJANGO_SETTINGS_MODULE'] = 'hrmd.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrmd.settings')

application = get_wsgi_application()
