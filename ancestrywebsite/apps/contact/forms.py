from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Name"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : "Email"}))
    phonenumber = PhoneNumberField(required=False, widget=PhoneNumberPrefixWidget(attrs={'class' : 'form-control', 'placeholder' : "Phone number"}), initial="+44")
    message = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Message", "rows": 5}))
