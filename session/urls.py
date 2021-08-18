from django.urls import path
from . import views
from django.contrib.auth.views import (PasswordResetDoneView, PasswordResetView,PasswordResetConfirmView,

                                    PasswordResetCompleteView)




urlpatterns = [

    path('login/',views.login_user,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('sign-up/',views.registration,name='signup'),
    path('password_change/',views.change_pass,name='change_password'),
    path('activate/<uidb64>/<token>/',views.activate_user_account,name='activate_ac'),

    # for built in  password  reset view 

    path('reset/password/',PasswordResetView.as_view(template_name='session/reset_pass.html'),name = 'password_reset'),
    path('reset/password/done/',PasswordResetDoneView.as_view(template_name='session/reset_password_done.html'),name = 'password_reset_done'),
    path('reset/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name='session/password_reset_confrim.html'),name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='session/password_reset_complete.html'),name = 'password_reset_complete'),

]