from django.db import models
import uuid
from django.contrib.auth.models import User


# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     slug = models.SlugField(unique=True)

#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     class Meta:
#         ordering = ['name', 'created'] 
    
#     def __str__(self):
#         if self.name:
#             return self.name



class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # task_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_pinned = models.BooleanField(default=False)
    pinned_at = models.DateTimeField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['-is_pinned', '-pinned_at', '-created'] 
    
    def __str__(self):
        if self.title:
            return self.title
