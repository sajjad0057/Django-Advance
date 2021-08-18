import django
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

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


