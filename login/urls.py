from django.urls import path, include
from . import views as userViews
from django.contrib.auth import views as authViews



urlpatterns = [
    path('registration/', userViews.reg, name='reg'),
    path('login/', authViews.LoginView.as_view(template_name='login/login.html',redirect_authenticated_user=True), name='login'),

    path('exit/', authViews.LogoutView.as_view(template_name='collection/home.html'), name='logout'),

    path('pass-reset/',authViews.PasswordResetView.as_view(template_name='login/pass-reset.html'), name='pass-reset'),
    path('password_reset_complete/',authViews.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset_confirm/<uid64>/<token>/',authViews.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done/',authViews.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
]
