# Minimal application

from celery import Celery

app = Celery('Hello', broker='amqp://guest@lacalhost//')

@app.task
def hello():
    return 'hallo world'
