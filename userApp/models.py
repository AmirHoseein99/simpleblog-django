from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Bio = models.TextField(max_length=200, blank=True)
    profile_pic = models.ImageField(
        default='/home/amirhossein/DjangoPractice/projects/simpleblog/files/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
