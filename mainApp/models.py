from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    date_of_creation = models.DateTimeField(
        default=timezone.now, auto_now=False, auto_now_add=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('mainApp:postpage', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_of_creation',)


class Comment(models.Model):

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
