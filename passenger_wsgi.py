# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1415184/data/www/flatm8.ru/room8d')
sys.path.insert(1, '/var/www/u1415184/data/room8e/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'room8d.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
