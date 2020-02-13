from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.


def mainPage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'mainApp/mainPage.html', context)


def aboutPage(request):
    return render(request, 'mainApp/aboutPage.html', {'title': 'About'})


def postPage(request):
    return HttpResponse("<p> post page </p>")
