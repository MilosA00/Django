from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


@csrf_exempt
def login(request):
    return render(request, "login.html")


@csrf_exempt
def login_request(request):
    if request.method == "POST":
        user = User.objects.all()
        # user.authenticate(user_name="123", password="123")

        for i in range(len(user)):
            if user[i].user_name == request.get("user_name"):
                if user[i].password == request.POST['password']:
                    return redirect("home")

        print(user.password)
        if user is not None:
            return redirect("home")
        else:
            return HttpResponse("Invalid login form")
        for user in user:
            print(form.__dict__)
            print(request.POST.__dict__)
            if user.user_name == request.POST.get('username', ""):
                if user.password == request.POST.get('password', ""):
                    return redirect("home")

        # if user.("user_name") == request.user.username:
        #     return redirect("home.html")
        # else:
        #     return HttpResponse("Username or password incorrect")

    form = UserForm()
    return render(request, "login.html", {"form": form})


@csrf_exempt
def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            return HttpResponse(request, status=400)


def home(request):
    users = User.objects.all()
    return render(request, "home.html", {"users": users})
