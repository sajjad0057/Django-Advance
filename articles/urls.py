from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('exception/',views.exception_view,name='exception'),
]