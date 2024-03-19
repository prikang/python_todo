from django.urls import path
from core2.views import ProductView
from core2.views import ContactView

urlpatterns = [
    path("products/",ProductView.as_view(),name="products"),
    path("contacts/",ContactView.as_view(),name="contacts")
]
