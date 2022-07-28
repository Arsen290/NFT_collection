from django.urls import path
from . import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('registration/', userViews.reg, name='reg'),
    path('login/', authViews.LoginView.as_view(template_name='login/login.html'), name='login'),
    #? path('exit/', authViews.LoginView.as_view(template_name='home.html'), name='logout'),
]
