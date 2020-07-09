from __future__ import absolute_import
from celery_proj import app

@app.task
def add(x,y):
    return x+y