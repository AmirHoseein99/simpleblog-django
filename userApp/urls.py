from django.urls import path
from . import views

app_name = 'userApp'
urlpatterns = [
    path('register/', views.user_register_page, name='userRegisterPage'),
]
