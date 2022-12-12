from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home1', views.home1, name='home1'),
    path('home2', views.home2, name='home2'),
    path('home3', views.home3, name='home3'),
    path('about', views.about, name='about')
]