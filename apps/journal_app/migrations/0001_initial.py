# Generated by Django 3.0.6 on 2020-10-28 01:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('page', models.PositiveIntegerField()),
                ('quote', models.CharField(max_length=60)),
                ('quote_author', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('alias', models.CharField(max_length=45)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(130)])),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Morning',
            fields=[
                ('day', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='morning', serialize=False, to='journal_app.Day')),
                ('grateful_first', models.CharField(max_length=60)),
                ('grateful_second', models.CharField(max_length=60)),
                ('grateful_third', models.CharField(max_length=60)),
                ('great_first', models.CharField(max_length=60)),
                ('great_second', models.CharField(max_length=60)),
                ('great_third', models.CharField(max_length=60)),
                ('affirmation', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Night',
            fields=[
                ('day', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='night', serialize=False, to='journal_app.Day')),
                ('amazing_first', models.CharField(max_length=60)),
                ('amazing_second', models.CharField(max_length=60)),
                ('amazing_third', models.CharField(max_length=60)),
                ('made_better', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('day', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='thought', serialize=False, to='journal_app.Day')),
                ('thought', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='journal_app.User'),
        ),
    ]
