import asyncio

from quart import Quart


app = Quart(__name__)


@app.route('/hello')
async def hello():
    await asyncio.sleep(10)
    return 'Hello'


@app.route('/user/<string:username>')
async def world(username):
    return f'Hi, {username}'


if __name__ == '__main__':
    app.run()
