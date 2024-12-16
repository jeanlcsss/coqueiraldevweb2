# orders/forms.py
from django import forms
from .models import Order, OrderItem

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

class OrderItemCreateForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
