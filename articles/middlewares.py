
'''
 following https://docs.djangoproject.com/en/3.2/topics/http/middleware/#marking-middleware-as-unused

'''
# middleware function name : 

def simple_middleware(get_response):
    # One-time configuration and initialization.

    print('this is example_middleware for testing ')

    #inner function name : 
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("articles middleware ---->  this is before view ")
        response = get_response(request)
        print("articles middleware ---->  this is after view ")

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware