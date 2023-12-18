from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='login', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)