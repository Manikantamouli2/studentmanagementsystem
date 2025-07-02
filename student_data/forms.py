from django import forms 
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {'fname': "First Name", 'lname': "Last Name", 'phone': "Phone no"}
        widgets = {
            'fname': forms.TextInput(attrs={"class": "form-control"}),
            'lname': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'phone': forms.NumberInput(attrs={"class": "form-control"}),
            'branch': forms.Select(attrs={"class": "form-control"}),
        }
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password (again)', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'})

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
