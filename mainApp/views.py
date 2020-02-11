from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.


def mainPage(request):
    return HttpResponse("<p> main page </p>")


def postPage(request):
    return HttpResponse("<p> post page </p>")
