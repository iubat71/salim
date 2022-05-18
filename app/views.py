from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.base import View

class First_Home(View):
    def get(self, request):
        
        return render(request, "index.html")
class Home(TemplateView):
    template_name = 'index.html'

def home (request):
    return render (request,'index.html')