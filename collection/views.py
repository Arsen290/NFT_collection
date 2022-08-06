from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import NFTCollection
from .forms import AddNFTForm
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    title = "Home page"
    return render(request, 'collection/home.html')


@login_required
def profile_redirect(request):
    if request.user.is_authenticated:
        slug = request.user.username
    return redirect('profile_slug',slug)

@login_required
def profile(request, slug):
    userRuequest = User.objects.filter(username=slug)[0]
    form=AddNFTForm()
    data={
        'NFT_Collection' : NFTCollection.objects.filter(collector=userRuequest.id),
        'useeeer' : userRuequest,
        "form": form,
        "user":slug,
    }
    if request.method == 'POST':
        form = AddNFTForm(request.POST)
        if form.is_valid():
            prf = form.save(commit=False)
            prf.collector = request.user
            prf.save()
        else:
            message['cred_err'] = True
    return render(request, 'collection/profile.html ', data)
