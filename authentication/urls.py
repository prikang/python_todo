from django.urls import path
from . views import register_view
from . views import save_view
urlpatterns=[
     path("register_page",register_view, name="register_page"),
      path("save_user",save_view, name="save_user"),
]