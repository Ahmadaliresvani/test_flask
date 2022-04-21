import datetime

import time

from flask import Flask, render_template, jsonify

app = Flask(__name__)


class UTC(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return datetime.timedelta(0)


@app.route('/update_time', methods=['POST'])
def update_time():
    new_time = datetime.datetime.now(UTC()).strftime('%H:%M:%S')
    return jsonify('', render_template('time_model.html', time=new_time))


@app.route("/")
def home():
    return render_template('home.html', time=time.time())


app.run()
