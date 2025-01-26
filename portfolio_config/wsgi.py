import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_config.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
