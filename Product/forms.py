from django import forms
from Product.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity','capital_price','selling_price','discount']
  