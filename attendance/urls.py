from django.urls import path
from .views import student
from . views import home_page
from . views import contact_page
urlpatterns=[
     path("student",student, name="student"),
     path("home", home_page, name="home_page"),
     path("contact", contact_page, name="contact"),
]