from django import forms
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'ville']
        widgets = {
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ville'}),
        }
