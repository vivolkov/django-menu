from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class RootView(TemplateView):
    template_name = 'django_menu/index.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, RootView.template_name)
