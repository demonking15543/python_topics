# Generated by Django 3.2 on 2022-11-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=300, verbose_name='Post Slug'),
        ),
    ]