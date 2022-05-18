from django.urls import path
from . import views
from . views import Home

urlpatterns = [
    path('', views.home,name='home_page'),
    path('home', views.Home.as_view(),name='class_home_page'),
    path('newhome', views.First_Home.as_view(),name='First_home_page'),


]
