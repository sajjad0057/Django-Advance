from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def exception_view(request):
    value = 1/0
    return HttpResponse("This is exception page")
