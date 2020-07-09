from __future__ import absolute_import
from celery import Celery

app = Celery('celery_proj',include=['celery_proj.tasks'])
app.config_from_object('celery_proj.celeryconfig')

if __name__ == "__main__":
    app.start()