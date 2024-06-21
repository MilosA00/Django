from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm
from .models import User


@csrf_exempt
def login(request):
    return render(request, "login.html")


def sigh_up(request):
    return render(request, "sign_up.html")


@csrf_exempt
def login_request(request):
    if request.method == "POST":
        user = User.objects.all()
        # user.authenticate(user_name="123", password="123")
        for i in range(len(user)):
            if user[i].user_name == request.POST.get("username"):
                if user[i].password == request.POST.get('password'):
                    return redirect("home")

    form = UserForm()
    return render(request, "login.html", {"form": form})


@csrf_exempt
def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

        else:
            return HttpResponse("NOK", status=400)

    return render(request, "sign_up.html")


def home(request):
    users = User.objects.all()
    return render(request, "home.html", {"users": users})
