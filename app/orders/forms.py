# coding=utf-8
from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # gender = forms.ChoiceField(choices=CHOISE, widget=forms.RadioSelect())

    class Meta(object):
        model = Order
        fields = ['name', 'phone', 'gender', 'email']


# class OrderConfirmForm(forms.ModelForm):
#     class Meta(object):
#         model = Order
#         fields = ['name', 'gender', 'email']
