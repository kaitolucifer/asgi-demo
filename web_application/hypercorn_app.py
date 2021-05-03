import os
import asyncio

from hypercorn.config import Config
from hypercorn.asyncio import serve


config = Config()
config.bind = ["localhost:5000"]
config.certfile = os.path.join(os.path.dirname(__file__), "ssl_certificate/cert.pem")
config.keyfile = os.path.join(os.path.dirname(__file__), "ssl_certificate/key.pem")


async def app(scope, receive, send):
    if scope["type"] == "lifespan":
        return
    if scope["type"] != "http":
        raise Exception("Only the HTTP protocol is supported")

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            (b'content-type', b'text/plain'),
            (b'content-length', b'5'),
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'hello world',
    })

if __name__ == '__main__':
    asyncio.run(serve(app, config))
