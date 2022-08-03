from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NFTCollection(models.Model):
    cardsUrl=models.URLField('Url')
    cardsName=models.CharField('Name NFT',max_length=20)
    cardsDescription=models.TextField('Description')
    collector=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'NFT name: {self.cardsName}'
    class Meta:
        verbose_name="NFTCollection"
        verbose_name_plural="NFTCollections"
