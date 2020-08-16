from django import forms
from .models import Sales

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['date', 'sold_to', 'item','quantity','status']


class InvoiceeForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['sold_to']

