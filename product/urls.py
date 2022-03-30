from django.urls import path
from .views import *
from product import views

urlpatterns = [
    path('get', views.get_product),
    path('get_cat', views.get_cat),
]