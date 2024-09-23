from django.core.cache import cache
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm
from .models import User

CACHE_TTL = getattr('settings.py', 'CACHE_TTL', 3600)


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
            return JsonResponse({'status': True})

        else:
            return JsonResponse({'status': False}, status=422)

    return render(request, "sign_up.html")


def home(request):
    if request.method == "GET":
        users = User.objects.all()
        result = []

        subject = cache.get('name')
        if not subject:
            for user in users:
                u = {"user_name": user.user_name, "password": user.password, "email": user.email}
                result.append(u)
            cache.set('name', result, 5)
            context = {'subject': cache.get('name')}

            return JsonResponse({'status': True, 'data': context})
        else:
            context = {'subject': cache.get('name')}
            return JsonResponse(context)

        # if subject:
        #     return render(request, "home.html", subject)

    return HttpResponse("NOK", status=400)


@csrf_exempt
def all_user_purge(request):
    if request.method == "POST":
        value = request.POST.get("value")
        if (int(value)) == (int(1)):
            users = User.objects.all()
            for user in users:
                user.delete()
            return JsonResponse({'status': True}, status=200)
        else:
            return JsonResponse({'status': False}, status=422)

    return JsonResponse({'status': False})


def random_users(request):
    try:
        user_name = "one"
        password = "two"
        result = []

        for i in range(100):
            u = {"user_name": user_name, "password": password, "email": user_name}
            result.append(u)
            form = UserForm(u)
            form.save()
            user_name += ","
            password += ","

        return JsonResponse({'status': True}, status=200)
    except:
        return JsonResponse({'status': False}, status=500)
