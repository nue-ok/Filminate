# Generated by Django 4.2.8 on 2024-05-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.CharField(max_length=4),
        ),
    ]