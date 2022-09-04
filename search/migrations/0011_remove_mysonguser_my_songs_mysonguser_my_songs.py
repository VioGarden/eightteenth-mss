# Generated by Django 4.1 on 2022-09-04 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_remove_mysonguser_annid_remove_mysonguser_artist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysonguser',
            name='my_songs',
        ),
        migrations.AddField(
            model_name='mysonguser',
            name='my_songs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='search.aotdata'),
        ),
    ]
