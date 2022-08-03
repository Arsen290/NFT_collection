from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import NFTCollection

# Create your views here.
def home(request):
    title = "Home page"
    return render(request, 'collection/home.html')

@login_required
def profile(request):
    data={
        'NFT_Collection' : NFTCollection.objects.all(),
    }
    return render(request, 'collection/profile.html ',data)
