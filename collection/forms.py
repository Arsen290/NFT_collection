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

class ownerForm(forms.Form):
    Owner = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control header-form text-center w-100"}),max_length=255)
    def __init__(self, *args, **kwargs):
        super(ownerForm, self).__init__(*args, **kwargs)
        self.fields['Owner'].label = ""
        self.fields['Owner'].widget.attrs['placeholder'] = "Owner"
        self.fields['Owner'].required = False
