from django.shortcuts import render
from attendance.models import Attendance
# Create your views here.

def student(request):
    record=Attendance.objects.all()
    context={
        "atten": record
    }

    return render(request,"attendance.html",context=context)

def home_page(request):
    return render(request,"home.html")

def contact_page(request):
    return render(request,"contact.html")
