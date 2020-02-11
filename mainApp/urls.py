from django.urls import path
from . import views

# app_name = 'mainApp'
urlpatterns = [
    path('main/', views.mainPage, name='mainpage'),
    path('post/', views.postPage, name='postpage')
]
