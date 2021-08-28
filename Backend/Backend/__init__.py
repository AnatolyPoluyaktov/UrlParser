# Django starts so that shared_task will use this app.
from .celery import app
celery=app