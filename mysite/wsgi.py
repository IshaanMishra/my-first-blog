"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application


path = os.path.expanduser('~/djangogirls/mysite')

#if path not in sys.path:
	#pass
	#sys.path.insert(0,path)


os.environ["DJANGO_SETTINGS_MODULE"] = 'mysite.settings'

application = get_wsgi_application()
