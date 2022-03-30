from django.urls import path
from .views import *
from order import views

urlpatterns = [
    path('get_cart/<int:pk>', views.get_cart_usr),
    path('add-to-cart/<int:pk>', views.add_to_cart),
]