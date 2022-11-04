from django import forms
from home.models import Universite, Faculte, Departement, Promotion


class UnivForm(forms.ModelForm):
    class Meta:
        model = Universite
        fields = ['name', 'picture', 'logo', 'about', 'url', 'contact']


class FacForm(forms.ModelForm):
    class Meta:
        model = Faculte
        fields = ['univ', 'name']


class DepForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['fac', 'name']


class PromForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['fac', 'dep', 'name']
