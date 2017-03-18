from flask import Flask, render_template, redirect
from utils import token
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import threading
import random
import push

app = Flask(__name__)
app.secret_key = token()
scheduler = BackgroundScheduler()

messages = ['Here and Now!', 'Attention!']
access_token = push.get_access_token('access_token')


def random_message():
	return random.choice(messages)


def myna(access_token):
	message = random_message()
	push.push_message(message, '', access_token)  # TODO: Error Handling?


scheduler.add_job(myna, 'interval', seconds=30, args=[access_token])


@app.route('/start', methods=['POST'])
def start():
	scheduler.resume()
	return redirect('/')


@app.route('/stop', methods=['POST'])
def stop():
	scheduler.pause()
	return redirect('/')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    scheduler.start()
    app.run(use_reloader=False)  # Necessary to avoid duplication of scheduler
