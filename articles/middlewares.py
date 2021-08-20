
'''
 following https://docs.djangoproject.com/en/3.2/topics/http/middleware/#marking-middleware-as-unused

'''
# middleware function name : 
from django.http import response
from django.shortcuts import redirect


# functional middleware : 

# def simple_middleware(get_response):
#     # One-time configuration and initialization.

#     print('this is simple_middleware for testing ')

#     #inner function name : 
#     def middleware(request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#         print("articles function based middleware ---->  this is before view ")
#         path = request.path
#         # set /sajjad or /nafiul or /ariful after host url , when this middle are redirect location url .
#         if path in ['/sajjad','/nafiul','/arif']:  
#             return redirect('location:user-location');
#         response = get_response(request)
#         print("articles function based middleware ---->  this is after view ")

#         # Code to be executed for each request/response after
#         # the view is called.

#         return response

#     return middleware





# Class Based Middleware : 

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print('this is simple_middleware for testing ')

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("articles class based middleware ---->  this is before view ")
        path = request.path
        # set /sajjad or /nafiul or /ariful after host url , when this middle are redirect location url .
        if path in ['/sajjad','/nafiul','/arif']:  
            return redirect('location:user-location');
        response = self.get_response(request)
        print("articles class based middleware ---->  this is after view ")

        # Code to be executed for each request/response after
        # the view is called.

        return response
