# Generated by Django 3.1.5 on 2021-06-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduHub', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(),
        ),
    ]