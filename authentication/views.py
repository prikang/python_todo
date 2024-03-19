from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib import messages

from authentication.forms import RegistrationForm
# Create your views here.
User= get_user_model()

def login_view(request):
    pass

def register_view(request):
    form= RegistrationForm
    context={
        "form":form
    }
    return render(request,"register.html", context=context)

def save_view(request):
    if request.method =="POST":
        form= RegistrationForm(data=request.POST)
        form.is_valid()
        data= form.cleaned_data
    try:
        # print(form.cleaned_data)
        user=User.objects.create(
            username= data.get("username"),
            first_name= data.get("first_name"),
            last_name= data.get("last_name"),
            email= data.get("email")
         
        )
        user.set_password(data.get("password"))
        user.save()
        messages.success(request,"User register successfully")
    except IntegrityError:
       messages.error(request,"User with this username already exist")

    return redirect('register_page')

    