from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings

#import redirect login УДАЛИСТЬ
# from django.urls import reverse
# from allauth.account.views import LoginView as AllauthLoginView
# from allauth.account.utils import get_next_redirect_url

# Create your views here.


def reg(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            loginAuth(request, new_user)
            messages.success(request, f'The owner {username} has been successfully created')
            return redirect('login') #Поменять путь перехода на логин
    else:
        form = UserRegisterForm()
    return render(request,'login/reg.html', {'title':'Registration', 'form':form})
