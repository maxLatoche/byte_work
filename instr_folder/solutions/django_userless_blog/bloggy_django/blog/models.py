from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=4000)
    slug = models.SlugField(max_length=40)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.updated_at = timezone.now()
        self.full_clean()
        if not self.id:
            self.created_at = timezone.now()
        super(Post, self).save(*args, **kwargs)

    def clean(self):
        min_validation(self.title)


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)


def min_validation(value):
    if len(value) < 5:
        raise ValidationError("{} is invalid, must have more than 5 characters". format(value))


    

