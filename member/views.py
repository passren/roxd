from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.forms.forms import NON_FIELD_ERRORS

from .forms import SigninForm, SignupForm
from .models import UserProfile
from django.contrib.auth.models import User

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

def signup(request):
    if request.user.is_authenticated():
        return redirect("/")
    
    if request.method=='POST':
        signupForm = SignupForm(request.POST)
        
        if signupForm.is_valid():
            username = signupForm.cleaned_data['username']
            email = signupForm.cleaned_data['email']
            phone = signupForm.cleaned_data['phone']
            password = signupForm.cleaned_data['password']
            passwordConfirmed = signupForm.cleaned_data['passwordConfirmed']
            
            if password <> passwordConfirmed:
                signupForm._errors[NON_FIELD_ERRORS] = signupForm.error_class(['Password are not matched.'])
            else:
                user = User.objects.create_user(username, email, password)
                userProfile = UserProfile(user=user, phone=phone, source=UserProfile.USER_SOURCE[0][0])
                userProfile.createUser()
                return render(request, "signupSuccess.html", {})
    else:
        signupForm = SignupForm()
    
    return render(request, "signup.html", {'form': signupForm})

def profile(request, username):
    return render(request, "profile.html")
