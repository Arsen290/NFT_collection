from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import NFTCollection
from .forms import AddNFTForm, ownerForm
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

from django.contrib import messages

# Create your views here.
def home(request):
    formss = ownerForm()

    if request.method == "POST":
        formss = ownerForm(request.POST)
        if formss.is_valid():
            ownervalue = formss.cleaned_data["Owner"]
            slug=str(ownervalue)
            return redirect('profile_slug', slug=slug)
    title = "Home page"
    data={'my_form': formss}
    return render(request, 'collection/home.html', data)


@login_required
def profile_redirect(request):
    if request.user.is_authenticated:
        slug = request.user.username
    return redirect('profile_slug',slug)

@login_required
def profile(request, slug):

    formss = ownerForm()
    if 'Owner' in request.POST:
        if request.method == "POST":
            formss = ownerForm(request.POST)
            if formss.is_valid():
                ownervalue = formss.cleaned_data["Owner"]
                slug=str(ownervalue)
                return redirect('profile_slug', slug=slug)

    userRuequest = User.objects.filter(username=slug)[0]
    form=AddNFTForm()
    data={
        'NFT_Collection' : NFTCollection.objects.filter(collector=userRuequest.id),
        'useeeer' : userRuequest,
        "form": form,
        "user":slug,
        'my_form': formss
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

#views function for delete card
def DeleteCardView(request, id):
    model = NFTCollection
    ob = model.objects.get(id=id)
    ob.delete()
    def test_func(self):
        cards=self.get_object()
        if self.request.user == cards.collector:
            return True
        return False
    return redirect('profile_slug', slug=request.user.username)

def Search(request,slug):
    if request.method == 'POST':
        slug = request.POST.get('slug')
        return slug
    return redirect('profile_slug', slug)
