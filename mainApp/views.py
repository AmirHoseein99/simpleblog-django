from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.


def main_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'mainApp/mainPage.html', context)


def about_page(request):
    return render(request, 'mainApp/aboutPage.html', {'title': 'About'})


def post_detail_page(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'mainApp/postdetailPage.html', {'post': post})
