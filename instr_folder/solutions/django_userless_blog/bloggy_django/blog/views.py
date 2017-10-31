from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from blog.forms import PostForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import View
import pudb


def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return redirect('/')


class UserLogin(View):

    template = "blog/login.html"

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect('/')

        else:
            return HttpResponse("you dont have an accoubnt@")


def register(request):
    if request.method == "GET":
        user_form = UserForm()
        user_profile_form = UserProfileForm()
        context = {
            'user_form': user_form,
            'user_profile_form': user_profile_form,
        }
        return render(request, "blog/register.html", context)
    if request.method == "POST":

        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():

            user_object = user_form.save()

            user_profile_object = user_profile_form.save(commit=False)

            user_profile_object.user = user_object

            user_profile_object.save()

        else:
            pass

        return redirect('blog:index')




def index(request):
    print(request.session.items())
    if request.method == "GET":
        all_posts = Post.objects.all().order_by('-updated_at')
        context = {
            "all_posts": all_posts
        }
        return render(request, "blog/index.html", context)


def add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:index")
        else:
            errors = form.errors.get('__all__')
            context = {
                "new_post_form": form,
                "errors": errors
            }
            return render(request, "blog/add.html", context)
    else:
        form = PostForm()
        context = {
            "new_post_form": form,
        }
        return render(request, "blog/add.html", context)


def edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:index")
        else:
            context = {
                "post": post,
                "edit_post_form": form,
            }
            return render(request, "blog/edit.html", context)
    else:
        form = PostForm(instance=post)
        context = {
            "post": post,
            "edit_post_form": form,
        }
        return render(request, "blog/edit.html", context)


def delete(request, id):
    if request.method == "POST":
        target_post = get_object_or_404(Post, id=id)
        target_post.delete()
    return redirect("blog:index")
