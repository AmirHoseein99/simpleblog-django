from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path
from django.contrib.auth import views as auth_view

app_name = 'userApp'
urlpatterns = [
    path('register/', views.user_register_page, name='userRegisterPage'),
    path('login/', auth_view.LoginView.as_view(template_name='userApp/loginPage.html'),
         name='userLoginPage'),
    path('logout/', auth_view.LogoutView.as_view(template_name='userApp/logoutPage.html'),
         name='userLogoutPage'),
    path('profile/', views.profile_page, name='userProfilePage'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
