import os

from werkzeug.serving import run_simple
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule


@Request.application
def app(request):
    urls = url_map.bind_to_environ(request.environ)
    endpoint, args = urls.match()
    request.environ['args'] = args
    return endpoint


@Request.application
def get_user(request):
    username = request.environ['args'].get('username')
    return Response(f'hello {username}')


url_map = Map([
    Rule('/<string:username>', endpoint=get_user, methods=['get'])
])


# 静的ファイルの配信
app = SharedDataMiddleware(app, {
    '/static/': os.path.join(os.path.dirname(__file__), 'static')})

if __name__ == '__main__':
    run_simple('localhost', 5000, app, use_debugger=True, use_reloader=True)
