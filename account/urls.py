from django.urls import path
from .views import *
from account import views

urlpatterns = [
    path('register', views.register_view),
    path('sign', CustomAuthToken.as_view()),
    path('users', views.get_all_user),
    path('profile/<int:pk>', views.user_profile)
]