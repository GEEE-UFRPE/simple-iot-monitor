from awesome_django_timezones.middleware import TimezonesMiddleware

class TimezoneMiddlewareWrapper:

    def __init__(self, get_response):
        self.awesome_django_timezone_middleware = TimezonesMiddleware(get_response)
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.method == 'GET':
            response = self.awesome_django_timezone_middleware.__call__(request)
        else:
            # When posting a new reading we don't need to know the timezone of the device.
            # Thus we can bypass the timezone middleware, reducing response time and
            # preventing unecessary calls to the IP api, which is subject to rate limiting.
            response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response