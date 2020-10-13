from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'home.html' )

def result(request):
    password = ""
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('number'):
        alphabets.extend(list("0123456789"))
    if request.GET.get('uppercase'):
        alphabets.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('special'):
        alphabets.extend(list("@#$_!_&?"))   

    for i in range(length):
        password += random.choice(alphabets)

    return render(request, 'result.html' , {'password': password})

def about(request):
    return render(request, 'about.html')