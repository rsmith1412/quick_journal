# Generated by Django 3.0.6 on 2020-12-18 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='page',
        ),
    ]