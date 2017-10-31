from django.shortcuts import render
from anagrams.models import Word

# Create your views here.

def index(request, word):
	return render(request, 'anagrams/index.html', {'word': word})