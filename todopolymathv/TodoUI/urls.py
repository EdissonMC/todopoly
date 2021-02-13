from django.urls import path
from . import views



app_name ='todoui'

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginPage, name="loginPage"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutUser, name="logout"),
  
]