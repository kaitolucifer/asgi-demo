from wsgiref.simple_server import make_server
import pprint


def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    pprint.pprint(environ)
    print(start_response)
    return [b'Hello World']


if __name__ == "__main__":
    with make_server('localhost', 5000, app) as httpd:
        httpd.serve_forever()
