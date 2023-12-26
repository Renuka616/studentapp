from django import forms
from .models import Customer,Vehicle
from django.core.exceptions import ValidationError

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ["created_at", "modified_at"]
    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"].strip()
        if not mobile.isdigit():
            raise ValidationError("Mobile number should be a digit.")
        if len(mobile) != 10:
            raise ValidationError("Mobile number should contains 10 digits.")
        if mobile[0] not in "6789":
            raise ValidationError("Mobile number should starts with '6789' digits.")
        return mobile

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"



class SignupForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

