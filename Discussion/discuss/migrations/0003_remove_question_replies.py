# Generated by Django 3.0.5 on 2020-04-14 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0002_auto_20200413_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='replies',
        ),
    ]
