from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.forms.forms import NON_FIELD_ERRORS

from .forms import SigninForm

# Create your views here.
def signin(request):
    if request.method=='POST':
        signinForm = SigninForm(request.POST)
        
        if signinForm.is_valid():
            username = signinForm.cleaned_data['username']
            password = signinForm.cleaned_data['password']
            user= auth.authenticate(username=username, password=password)
        
            if user is not None:
                if user and user.is_active:
                    auth.login(request, user)
                    return redirect("/")
                else:
                    signinForm._errors[NON_FIELD_ERRORS] = signinForm.error_class(['User is not active.'])
            else:
                signinForm._errors[NON_FIELD_ERRORS] = signinForm.error_class(['Username or password is not correct.'])
    else:
        signinForm = SigninForm()

    return render(request, "signin.html", {'form': signinForm})
    
def logout(request):
    auth.logout(request)
    return redirect("/")

def signup(reqest):
    pass
