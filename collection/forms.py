from django import forms
from .models import NFTCollection

class AddNFTForm(forms.ModelForm):
    # cardsUrl=forms.URLField()
    # cardsName=forms.CharField(max_length=30)
    # cardsDescription=forms.TextField(max_length=255)
    # collector=forms.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        model = NFTCollection
        fields = ['cardsUrl', 'cardsName', 'cardsDescription']
