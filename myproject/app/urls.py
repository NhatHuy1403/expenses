from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import home, expenses, checkout

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('home/', views.home,name="home"),
    path('expenses/', views.expenses,name="expenses"),
    path('checkout/', views.checkout,name="checkout"),
    
]
