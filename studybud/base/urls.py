from django.urls import path

from . import views

urlpatterns = [

    path("home", views.home, name="home"),
    path("user/login", views.login, name="login"),
    path("user/signup", views.sigh_up, name="sign_up"),

]
