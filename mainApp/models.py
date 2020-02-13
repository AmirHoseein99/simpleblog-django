from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    date_of_creation = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('mainApp:postpage', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_of_creation',)
