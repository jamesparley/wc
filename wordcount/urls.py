from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('count/', views.count, name='cnt'),
    path('about/', views.about, name='about'),
]
