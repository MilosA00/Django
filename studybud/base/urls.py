from django.urls import path

from . import views

urlpatterns = [

    path("home", views.home, name="home"),
    path("user/login", views.login, name="login"),
    path("user/login_request", views.login_request, name="login_request"),
    path("user/signup", views.sigh_up, name="sigh_up"),
    path("user/add_user", views.add_user, name="add_user"),

]
