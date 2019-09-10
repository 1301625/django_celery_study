from __future__ import absolute_import

import os
import djcelery
from celery import Celery
from datetime import timedelta
djcelery.setup_loader()

BROKER_URL = os.environ.get('RABBITMQ_HOST', "amqp://guest@localhost//")

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'periodic_tasks': {
          'task': 'posts.tasks.world',
          'schedule': timedelta(seconds=10),
    }
}
#os.environ.setdefault('DJANGO_SETINGS_MODUL', 'config.settings')

#app = Celery('config')

#app.config_from_object('django.conf:settings', namespace='CELERY')
#app.autodiscover_tasks()  # 자동으로


