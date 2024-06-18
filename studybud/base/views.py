from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserForm
from .models import User
from django.views.decorators.csrf import csrf_exempt


def login(request):
    return render(request, "login.html")


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
