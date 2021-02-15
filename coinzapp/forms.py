from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateDetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['full_name', 'phone_number', 'referral_id']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {'username': None,}


class UpdateDetailForm(forms.ModelForm):
    full_name = forms.CharField(required=False, label='Full Name')
    phone_number = forms.CharField(required=False, label='Phone Number')
    
    class Meta:
        model = Detail
        fields = ['full_name', 'phone_number']


class BasicForm(forms.ModelForm):
    vendor_id = forms.CharField(required=True,)
    coupon = forms.CharField(required=True,)

    class Meta:
        model = BasicOption
        fields = ['vendor_id', 'coupon', 'select_package']


class AdvancedForm(forms.ModelForm):
    vendor_id = forms.CharField(required=True,)
    coupon = forms.CharField(required=True,)

    class Meta:
        model = AdvancedOption
        fields = ['vendor_id', 'coupon', 'select_package']


class PremiumForm(forms.ModelForm):
    vendor_id = forms.CharField(required=True,)
    coupon = forms.CharField(required=True,)
    
    class Meta:
        model = PremiumOption
        fields = ['vendor_id', 'coupon', 'select_package']