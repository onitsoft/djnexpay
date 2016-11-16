# -*- coding: utf-8 -*-

from django import forms
from core.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = [
            'order_number',
            'is_paid',
            'is_released',
            'is_completed',
            'is_failed',
            'deleted',
            'disabled']


class DateSearchForm(forms.Form):
    date = forms.DateField(required=False, label="Search by Date")
