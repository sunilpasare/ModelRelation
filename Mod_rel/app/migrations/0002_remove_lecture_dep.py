# Generated by Django 3.2.7 on 2021-09-11 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='dep',
        ),
    ]
