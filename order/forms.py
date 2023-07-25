from django import forms
from django.core.exceptions import ValidationError

from order.models import Order


class OrderConfirmByUserForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["address"]
