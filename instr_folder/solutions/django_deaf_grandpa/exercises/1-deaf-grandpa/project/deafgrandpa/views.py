from django.shortcuts import render, redirect
import pudb

# Create your views here.

def index(request):
	saying = request.GET.get('saying',None)
	return render(request, 'deafgrandpa/index.html', {'grandpa_says': saying})


def say(request):
    if request.POST['say_to_grandpa'].isupper():
        saying = 'correct response, insert sarcasm here'
    else:
        saying = "What, I can't hear you Sonny!"
    return redirect('/?saying={}'.format(saying))
