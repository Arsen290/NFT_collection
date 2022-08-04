from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import NFTCollection
from .forms import AddNFTForm

# Create your views here.
def home(request):
    title = "Home page"
    return render(request, 'collection/home.html')

@login_required
def profile(request):
    form=AddNFTForm()
    data={
        'NFT_Collection' : NFTCollection.objects.filter(collector=request.user.id),
        "form": form
    }
    if request.method == 'POST':
        form = AddNFTForm(request.POST)
        if form.is_valid():
            prf = form.save(commit=False)
            prf.collector = request.user
            prf.save()

    return render(request, 'collection/profile.html ',data)
