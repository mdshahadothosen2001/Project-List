import logging


logger = logging.getLogger(__name__)


class RequestLoggerMiddleware:
    """used middleware concept for request and response api, and print for test.
    here have authentication, security, session, common, and custom middleware"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("RequestLoggerMiddleware: Before view")

        response = self.get_response(request)

        print("RequestLoggerMiddleware: After view")

        return response
