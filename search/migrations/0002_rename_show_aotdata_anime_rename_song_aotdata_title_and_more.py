# Generated by Django 4.1 on 2022-09-01 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aotdata',
            old_name='show',
            new_name='anime',
        ),
        migrations.RenameField(
            model_name='aotdata',
            old_name='song',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='aotdata',
            name='h480',
        ),
        migrations.RemoveField(
            model_name='aotdata',
            name='h720',
        ),
        migrations.RemoveField(
            model_name='aotdata',
            name='mp3',
        ),
        migrations.RemoveField(
            model_name='aotdata',
            name='opedin',
        ),
    ]
