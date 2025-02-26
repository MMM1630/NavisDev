import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
\
app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# app.conf.beat_schedule = {
#     'fetch-transaction-history-every-10-seconds': {
#         'task': 'your_app.tasks.fetch_transaction_history',
#         'schedule': 10.0, 
#     },
# }

app.conf.timezone = 'UTC'