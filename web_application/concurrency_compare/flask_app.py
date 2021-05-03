import time

from flask import Flask


app = Flask(__name__)


@app.route('/hello')
def hello():
    time.sleep(10)
    return 'Hello'


@app.route('/user/<string:username>')
def world(username):
    return f'Hi, {username}'


if __name__ == '__main__':
    app.run(threaded=False)
