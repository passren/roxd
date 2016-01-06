from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    remember = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    
class SignupForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(widget=forms.EmailInput, required=True)
    phone = forms.CharField(max_length=20, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    passwordConfirmed = forms.CharField(widget=forms.PasswordInput, required=True)