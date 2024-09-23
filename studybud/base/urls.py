from django.urls import path

from . import views

urlpatterns = [

    path("home", views.home, name="home"),
    path("all_user_purge", views.all_user_purge, name="all_user_purge"),
    path("user/login", views.login, name="login"),
    path("user/signup", views.sigh_up, name="sigh_up"),

]
