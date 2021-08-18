import django
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from .forms import signUpForm


# for mail varification :
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, message
from django.template.loader import render_to_string


# Create your views here.


def login_user(request):
    if request.method == "POST" :
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse('you are not valid!')
        else:
            return HttpResponse("form is not valid")

    else:
        form  = AuthenticationForm()
    
    return render(request,'session/login.html',{'form':form})



def user_logout(request):
    logout(request)
    return HttpResponse('you are logout successfully !')



def registration(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)  # domain name of requested site 
            mail_subject = 'An account Created'
            message = render_to_string('session/account.html',{'user':user,'domain':current_site.domain})  # convert html to string 
            send_mail = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject,message,to=[send_mail])
            email.send()
            # notification 
            return redirect('login')
        else:
            return HttpResponse("form is not valid")

    else:
        form = signUpForm()

    return render(request,'session/signup.html',{'form':form})



def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return HttpResponse("your password changed successfully !")
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request,'session/change_pass.html',{'form':form})










