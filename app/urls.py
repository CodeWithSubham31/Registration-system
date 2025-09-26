from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path("",views.home,name="home"),
    path("user_signup",views.user_signup,name="sign up"),
    path("user_signin",views.user_signin,name="sign in"),
    path("user_logout",views.user_logout,name="log out"),
]