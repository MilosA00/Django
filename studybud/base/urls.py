from django.urls import path
from . import views

urlpatterns = [

    path("home", views.home, name="home"),
    path("user/login", views.login, name="login"),
    path("user/login_request", views.login_request, name="login_request"),
    path("user/add", views.add_user, name="add_user"),

]
