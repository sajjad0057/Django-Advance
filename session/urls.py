from django.urls import path
from . import views


app_name = 'session' 

urlpatterns = [

    path('login/',views.login_user,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('sign-up/',views.registration,name='signup'),

]