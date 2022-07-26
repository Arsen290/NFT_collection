from django.shortcuts import render


# Create your views here.
def home(request):
    title = "Home page"
    return render(request, 'collection/home.html')
