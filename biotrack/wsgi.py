import os, sys

sys.path.append('/home/multidev/apps_wsgi')

sys.path.append('/home/multidev/apps_wsgi/biotrack')

os.environ['DJANGO_SETTINGS_MODULE'] = 'biotrack.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
