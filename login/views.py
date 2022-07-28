from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
def login(request):
    pass

def reg(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'The owner {username} has been successfully created')
            return redirect('home') #Поменять путь перехода на логин
    else:
        form = UserRegisterForm()
    return render(request,'login/reg.html', {'title':'Registration', 'form':form})
