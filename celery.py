from __future__ import absolute_import
from celery import Celery

app = Celery('celery_demo',include=['celery_demo.tasks'])
app.config_from_object('celery_demo.celeryconfig')

if __name__ == "__main__":
    #冲突测试2
    app.start()
