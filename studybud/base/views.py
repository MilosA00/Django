from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm
from .models import User


@csrf_exempt
def login(request):
    if request.method == "POST":
        user = User.objects.all()
        for i in range(len(user)):
            if user[i].user_name == request.POST.get("username"):
                if user[i].password == request.POST.get('password'):
                    return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False}, status=400)
    return render(request, "login.html")


@csrf_exempt
def sigh_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

        else:
            return HttpResponse("NOK", status=400)

    return render(request, "sign_up.html")


def home(request):
    if request.method == "GET":
        users = User.objects.all()
        result = []
        for user in users:
            u = {"user_name": user.user_name, "password": user.password, "email": user.email}
            result.append(u)
        return JsonResponse(result, safe=False)

    return HttpResponse("NOK", status=400)
