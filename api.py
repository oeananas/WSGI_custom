from webob import Request, Response


class Api:
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            if path == request_path:
                return handler

    def handle_request(self, request):
        response = Response()
        handler = self.find_handler(request_path=request.path)
        if handler is not None:
            handler(request, response)
        else:
            self.default_response(response)
        return response

    @staticmethod
    def default_response(response):
        response.status_code = 404
        response.text = 'Page not found :('
