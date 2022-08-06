# Generated by Django 4.0.6 on 2022-08-03 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NFTCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardsUrl', models.URLField(verbose_name='Url')),
                ('cardsName', models.CharField(max_length=20, verbose_name='Name NFT')),
                ('cardsDescription', models.TextField(verbose_name='Description')),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]