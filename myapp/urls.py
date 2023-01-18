from django.urls import path, include, reverse_lazy
from . import views
from .views import  Homepage
from django.contrib.auth import views as auth_views


app_name = "main"


urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    #path('mail/', Mail.as_view(), name="mail"),
    


    path("login/", auth_views.LoginView.as_view(template_name='main/login_page.html'), name='login_request'),

    path("logout/", auth_views.LogoutView.as_view(template_name='main/logout_page.html'), name='logout_request'),

    path("register_user/", views.register_user, name='register_user'),

    #path("change_password/", PasswordChange.as_view(success_url=reverse_lazy('main:login_request'),template_name='main/change_password.html'), name='change_password'),

    
    

    

] 
