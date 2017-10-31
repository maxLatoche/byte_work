from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    task = models.TextField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(null=True, blank=True, default=None)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.created_at = timezone.now()

        super(Todo, self).save(*args, **kwargs)

    def jeff_delete(self):
        self.deleted = True
        self.save()


    def __str__(self):
        return self.task
