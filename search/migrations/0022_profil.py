# Generated by Django 4.1 on 2022-09-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0021_userlist_profilescore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=100)),
                ('emai', models.CharField(max_length=100)),
                ('bi', models.CharField(max_length=100)),
            ],
        ),
    ]
