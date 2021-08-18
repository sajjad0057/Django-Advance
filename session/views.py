from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash,get_user_model
from django.contrib.auth.models import User
from .forms import signUpForm


# for mail varification :
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, message
from django.template.loader import render_to_string

# active a/c with email varification
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode


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
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)  # domain name of requested site 

            mail_subject = 'For active your account'

            message = render_to_string('session/account.html',{
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user)
                })  # convert html to string 

            send_mail = form.cleaned_data.get('email')

            email = EmailMessage(mail_subject,message,to=[send_mail])

            email.send()

            # notification  write here ....

            return redirect('login')
        else:
            return HttpResponse("form is not valid")

    else:
        form = signUpForm()

    return render(request,'session/signup.html',{'form':form})




def activate_user_account(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model()._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
        return HttpResponse("Some thing error , dosenot active your account ")
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()


        return HttpResponse("your account in Activated Now , Enjoy Now Here ")

    else:
        return HttpResponse("activation is invalid")








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










