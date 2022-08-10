from django.urls import path
from . import views
from django.contrib.auth import views as authViews


urlpatterns = [
    path('', views.home, name="home"),
    #realization redirect to profile_slug
    path('profile/', views.profile_redirect, name="profile"),
    path('profile/<slug:slug>/', views.profile, name="profile_slug"),
    path('profile/delete/<int:id>/ ', views.DeleteCardView, name="delete_card"),
]
