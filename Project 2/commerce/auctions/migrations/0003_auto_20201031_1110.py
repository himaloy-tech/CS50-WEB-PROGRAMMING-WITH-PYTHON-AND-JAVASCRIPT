# Generated by Django 3.0.7 on 2020-10-31 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='thumbnails'),
        ),
    ]
