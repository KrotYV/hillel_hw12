import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_12.settings')

app = Celery('hw_12')

app.config_from_object('hw_12.settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'task_celery_beat': {
        'task': 'celery_beat.tasks.parser_for_page',
        'schedule': crontab(minute=0, hour='1-23/2')
    }
}
