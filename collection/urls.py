from django.urls import path
from . import views
from django.contrib.auth import views as authViews


urlpatterns = [
    path('', views.home, name="home"),
    path('profile', views.profile, name="profile"),

]
