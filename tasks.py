from celery import Celery

# sqlite (filename)
BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'

app = Celery('tasks', broker=BROKER_URL)  # fill in broker

@app.task
def add(x, y):
	return x + y