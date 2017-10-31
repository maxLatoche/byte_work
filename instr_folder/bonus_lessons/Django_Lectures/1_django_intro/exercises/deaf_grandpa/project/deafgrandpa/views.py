from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'deafgrandpa/index.html')

def say(request):
    pass