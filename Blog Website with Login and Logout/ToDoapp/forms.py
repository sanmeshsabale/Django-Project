from django import forms
from .models import Tododata,Retrivedata

class RegistrationForm(forms.Form):
    name=forms.CharField(
        label="Enter your name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    email=forms.EmailField(
        label="Enter your Email:",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email'
            }
        )
    )
    password=forms.CharField(
        label="Enter your password:",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'your password'
            }
        )
    )
class LoginForm(forms.Form):
    name=forms.CharField(
        label="Enter your name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name',
            }
        )
    )
    password=forms.CharField(
        label="Enter your password:",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'your password'
            }
        )
    )
class InsertDataForm(forms.Form):
    blog_name=forms.CharField(
        label="Enter Blog name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Blog title here'
            }
        )
    )
    blog_description=forms.CharField(
        label="Enter Blog Content:",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Blog Content here'
            }
        )

    )
    ur_name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name here'
            }
        )
    )


class UpdateDataForm(forms.Form):
    blog_name=forms.CharField(
        label="Enter Blog name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter title here'
            }
        )
    )
    blog_description=forms.CharField(
        label="Enter blog Content",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'enter description here'
            }
        )
    )
    ur_name=forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name here'
            }
        )
    )

class DeleteDataForm(forms.Form):
    blog_name=forms.CharField(
        label="Enter Blog name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter Blog Name'
            }
        )
    )
