from django.urls import path
from .views import detail_page
from .views import register_page
from .views import login_page
from .views import home_page
from .views import about_page
from .views import my_todo
from .views import my_profile
from .views import todo_view
from .views import save_todo
from .views import login_view
from .views import auth_login
from .views import logout_view
urlpatterns=[
    path("detail",detail_page, name="detail"),
    path("register",register_page, name="register"),
    path("login",login_page, name="login"),
    path("",home_page),
    path("about",about_page, name="about"),
    path("mytodo",my_todo, name="mytodo"),
    path("profile",my_profile, name="profile"),
    path("todo_view",todo_view, name="todo_view"),
    path("login_view",login_view, name="login_view"),
    path("auth_login",auth_login, name="auth_login"),
    path("logout_view",logout_view, name="logout_view")

]