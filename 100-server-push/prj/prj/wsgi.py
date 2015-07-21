"""
WSGI config for prj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from geventwebsocket.handler import WebSocketHandler
from gunicorn.workers.ggevent import GeventPyWSGIWorker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prj.settings")

application = get_wsgi_application()


class Worker(GeventPyWSGIWorker):
    wsgi_handler = WebSocketHandler

    def handle_quit(self, *args):
        exit()
