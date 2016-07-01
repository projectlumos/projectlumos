# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_auto_20160629_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualityFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('helpfulness', models.FloatField(default=0)),
                ('simplicity', models.FloatField(default=0)),
                ('placement', models.FloatField(default=0)),
                ('recommendation', models.FloatField(default=0)),
                ('aggr_calculation', models.BooleanField(default=False)),
                ('resource', models.ForeignKey(to='learn.Resources')),
            ],
            options={
                'db_table': 'quality_feedback',
            },
        ),
    ]
