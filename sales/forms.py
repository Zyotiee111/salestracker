from django import forms
from sales.models import Sales

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = "__all__"