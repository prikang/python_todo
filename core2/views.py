from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.

class ProductView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"product.html")

    def post(self,request,*args,**kwargs):
        pass


class ContactView(TemplateView):
    template_name="contact.html"