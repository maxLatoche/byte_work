from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Post
from posts.forms import PostForm
from django.views.generic import View
from django.core.exceptions import ValidationError

def posts_list(req):
	whiskey_list = Post.objects.all()
	context = {
		"whiskey_list" : whiskey_list,
	}
	return render(req, "posts/list.html", context)

def posts_create(req):
	create_form = PostForm(req.POST or None)

	if create_form.is_valid():
		instance = create_form.save(commit=False)
		instance.save()
		return redirect(instance)
	context = {
		"create":create_form,
	}
	return render(req, "posts/create.html", context)

def posts_detail(req, id=None):
	whiskey = get_object_or_404(Post, id=id)
	print(whiskey.id)
	context = {
		"whiskey": whiskey
	}
	return render(req, "posts/detail.html", context)

def posts_update(req, id=None):

	whiskey = get_object_or_404(Post, id=id)

	update_form = PostForm(req.POST or None, instance = whiskey)
	print(update_form)
	if update_form.is_valid():
		instance = update_form.save()
		return redirect(instance)
	context = {
		"whiskey": update_form,
	}
	return render(req, "posts/update.html", context)

def posts_delete(req, id=None):

	instance=get_object_or_404(Post, id=id)
	instance.delete()
	return redirect('posts:list', permanent=True)



