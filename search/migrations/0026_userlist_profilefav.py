# Generated by Django 4.1 on 2022-09-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0025_delete_profil'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='ProfileFav',
            field=models.BooleanField(default=False),
        ),
    ]