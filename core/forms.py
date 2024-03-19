from django import forms


class AddTodoForm(forms.Form):
    title = forms.CharField(max_length=27)
    description = forms.CharField(max_length=127)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=27)
    password = forms.CharField(widget=forms.PasswordInput())
   
