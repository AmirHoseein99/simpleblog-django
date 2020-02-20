from django.urls import path
from . import views

app_name = 'mainApp'
urlpatterns = [
    path('', views.main_page, name='mainpage'),
    path('about/', views.about_page, name='aboutpage'),
    path('createpost/', views.create_post_page, name='createPostPage'),
    path('<slug:post>/', views.post_detail_page, name='postpage'),
    path('updatepost/<slug:post>/',
         views.update_post_page, name='updatePostPage'),
    path('deletepost/<slug:post>/',
         views.delete_post_page, name='deletePostPage'),

]
