# Generated by Django 4.1 on 2022-09-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AotData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('annid', models.IntegerField()),
                ('show', models.CharField(max_length=200)),
                ('opedin', models.CharField(max_length=25)),
                ('h720', models.CharField(max_length=100)),
                ('h480', models.CharField(max_length=100)),
                ('mp3', models.CharField(max_length=100)),
            ],
        ),
    ]
