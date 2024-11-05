from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]

        # adding labels
        labels = {
                "name": "Product Name",
                "description": "Product Usage",
                "price": "Cost in Dollars"
                }

