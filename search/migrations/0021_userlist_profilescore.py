# Generated by Django 4.1 on 2022-09-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0020_remove_userlist_profilescore_delete_songscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='ProfileScore',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
