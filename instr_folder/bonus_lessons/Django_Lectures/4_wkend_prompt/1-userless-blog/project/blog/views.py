from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import Post
from blog.forms import PostForm

# Create your views here.

class IndexView(View):
	template = 'blog/index.html'
	pass
