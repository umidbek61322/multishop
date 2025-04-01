from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from shop.models import CustomUser

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Re-password"
    }))

    class Meta:
        model = CustomUser
        fields = ["email","first_name","phone_number","country"]
        widgets = {
            "email":forms.EmailInput(attrs={
                "class":"form-control",
                "placeholder":"Email"
            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"First name"
            }),
            "phone_number":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Phone number"
            }),
            "country":forms.Select(attrs={
                "class":"form-control"
            })
        }

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                "class":"form-control",
                "placeholder":"email"
            }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                "class":"form-control",
                "placeholder":"password"
            }))
    class Meta:
        model = CustomUser
        fields = ["email","password"]

        