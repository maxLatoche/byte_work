from django import forms
from django.forms import Textarea
from blog.models import Post, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].validators.append(min_validation)
        
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
        widgets = {
            "content": Textarea(attrs={"cols": 50, "rows": 10}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
        widgets = {
            "content": Textarea(attrs={"cols": 50, "rows": 10}),
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'website'
        ]

def min_validation(value):
    if len(value) < 5:
        raise ValidationError("{} is invalid, must have more than 5 characters". format(value))

