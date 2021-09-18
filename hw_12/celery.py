import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_12.settings')

app = Celery('hw_12')

app.config_from_object('hw_12.settings', namespace='CELERY')

app.autodiscover_tasks()
