# Generated by Django 4.0.1 on 2022-03-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]