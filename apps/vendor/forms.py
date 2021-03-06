from django.forms import ModelForm, fields
from apps.product.models import Product, ProductImage


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']


class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
