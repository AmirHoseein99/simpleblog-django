from django.urls import path
from . import views

app_name = 'mainApp'
urlpatterns = [
    path('', views.main_page, name='mainpage'),
    path('about/', views.about_page, name='aboutpage'),
    path('<slug:post>/', views.post_detail_page, name='postpage'),
]
