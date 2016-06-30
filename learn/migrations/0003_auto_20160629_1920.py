# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_auto_20160626_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='quality_helpfulness',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resources',
            name='quality_placement',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resources',
            name='quality_recommendation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resources',
            name='quality_simplicity',
            field=models.IntegerField(default=0),
        ),
    ]
