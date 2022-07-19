from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *

class CardCreationForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'