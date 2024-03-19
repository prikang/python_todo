from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Todo
from core.models import Profile
from core.forms import AddTodoForm
from django.contrib import messages
from django.db import IntegrityError
from core.forms import LoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


# Create your views here.

def detail_page(request):
    return HttpResponse("This is detail page")

def register_page(request):
    return HttpResponse("This is register page")

def login_page(request):
    return HttpResponse("This is login page")

def home_page(request):
    # context={
    #     "user_name":"Prikang",
    #     "address":"Banasthali",
    #     "quote":"Yes"
    # }
    print(timezone.now())
    queryset=Todo.objects.all()
    context={
        "user_name":"Prikang",
        "queryset":queryset
       
    }

    return render(request,"index.html",context=context)


def about_page(request):
    context={
        "company_name":"leapfrog",
        "object":{
            "name":"Rajesh",
            "Caste":"Pulami"
        },
        "list_of_item":[{"name":"prikang","age":22,"position":"vocalist"},{"name":"Jungkook","age":26,"position":"vocalist"}]
    }
    return render(request,"about.html",context=context)

def my_todo(request):
    # print(request.GET)
    todo=request.GET.get("mytodo")
    if todo=="past":
         queryset=Todo.objects.filter(
             date_time__lte=timezone.now()
         )
    else:
         queryset=Todo.objects.filter(
            date_time__gte=timezone.now()
         )
         

    print(timezone.now())
    # queryset=Todo.objects.all()
    context={
        "queryset":queryset
    }
    return render(request,"my_todo.html",context=context)
@login_required (login_url="login_view")
def my_profile(request):
    queryset1=Profile.objects.all().first()
    context={
        "queryset1":queryset1
    }
    return render(request,"my_todo.html",context=context)


def todo_view(request):
    form=AddTodoForm
    context={
        "form":form
    }
    return render(request,"todo.html",context=context)

def save_todo(request):
    if request.method =="POST":
        form= AddTodoForm(data=request.POST)
        form.is_valid()
        data= form.cleaned_data
        
    # try:
        # print(form.cleaned_data)
        Todo.objects.create(
            title= data.get("title"),
            description= data.get("description"),
            user_id=1,
            date_time=timezone.now()
            
        )
        messages.success(request,"Todo is saved")
    # except IntegrityError:
    #    messages.error(request,"Todo is not saved")

    return redirect('todo_view')

def login_view(request):
    form= LoginForm
    context={
        "form":form
    }
    return render(request,"login.html", context=context)

def auth_login(request):
    if request.method=="POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request,user)
                return redirect("profile")
            else:
                messages.error(request,"wrong password")
                return redirect("login_view")

def logout_view(request):
    logout(request)
    return redirect("login_view")
