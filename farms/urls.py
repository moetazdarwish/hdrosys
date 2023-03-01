

from django.urls import path, include
from . import views

urlpatterns = [
    # path('getCategory/', views.getCategory, name="getCategory"),
    path('loginUser/', views.loginUser, name="loginUser"),

]
