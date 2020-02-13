from django.urls import path
from . import views

# app_name = 'mainApp'
urlpatterns = [
    path('', views.mainPage, name='mainpage'),
    path('about/', views.aboutPage, name='aboutpage'),
    path('post/', views.postPage, name='postpage'),
]
