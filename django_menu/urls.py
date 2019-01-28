from django.urls import path

from .views import RootView

app_name = 'django_menu'

urlpatterns = [
    path('', RootView.as_view(), name='home'),
#    path(),
] 
