from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, ValidationError
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
                raise ValidationError("Email exists")
        return email

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email != self.instance.email:
            if User.objects.filter(email=email).exists():
                    raise ValidationError("Email exists")
        return email

class ProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']