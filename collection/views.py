from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    title = "Home page"
    return render(request, 'collection/home.html')

@login_required
def profile(request):
    return render(request, 'collection/profile.html ')
