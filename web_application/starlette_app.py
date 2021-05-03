import os
import asyncio
import random

from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.responses import JSONResponse, HTMLResponse
import uvicorn


async def user(request):
    username = request.path_params['username']
    return HTMLResponse(f'<html><body>Hello {username}</body></html>')


async def ws_endpoint(websocket):
    await websocket.accept()
    print(await websocket.receive_text())
    await websocket.send_text('hello from ws server')
    for _ in range(10):
        await asyncio.sleep(random.randint(1, 3))
        await websocket.send_text(f'lucky number {random.randint(1, 100)}')
    await websocket.close()


async def json_endpoint(request):
    return JSONResponse({"message": "Hello"})


routes = [
    Route('/user/{username}', user),
    WebSocketRoute('/ws', ws_endpoint),
    Route('/json', json_endpoint),
    Mount('/static',
          StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'static'))),
]

app = Starlette(debug=True, routes=routes)


if __name__ == "__main__":
    uvicorn.run("starlette_app:app", host="127.0.0.1", port=5000, log_level="info")
