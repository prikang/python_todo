from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=27)
    first_name = forms.CharField(max_length=27)
    last_name = forms.CharField(max_length=27)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

