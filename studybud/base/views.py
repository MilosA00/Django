from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader



def login(request):
    return render(request, "login.html")