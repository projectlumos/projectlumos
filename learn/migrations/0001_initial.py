# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('desc', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'domain',
            },
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('desc', models.TextField(null=True, blank=True)),
                ('link', models.CharField(max_length=100)),
                ('diff_level', models.IntegerField(blank=True, null=True, choices=[(0, b'Beginner'), (1, b'Intermediate'), (2, b'Advanced')])),
                ('diff_sort', models.IntegerField(default=999)),
                ('media_type', models.IntegerField(default=3, choices=[(0, b'Video'), (1, b'Article'), (2, b'Interactive Site'), (3, b'Other')])),
                ('slug', models.SlugField()),
                ('domain', models.ManyToManyField(to='learn.Domain')),
            ],
            options={
                'db_table': 'resources',
                'verbose_name_plural': 'resources',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('desc', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'technology',
                'verbose_name_plural': 'technologies',
            },
        ),
        migrations.AddField(
            model_name='resources',
            name='technology',
            field=models.ManyToManyField(to='learn.Technology'),
        ),
        migrations.AddField(
            model_name='domain',
            name='technology',
            field=models.ManyToManyField(to='learn.Technology'),
        ),
    ]
