from django.urls import path
from . import views


app_name = 'location'

urlpatterns = [
    path('user/',views.UserLocationAPI.as_view(),name='user-location')

]