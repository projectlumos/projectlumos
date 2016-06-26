# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='is_youtube',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='resources',
            name='diff_level',
            field=models.IntegerField(default=None, choices=[(0, b'Beginner'), (1, b'Intermediate'), (2, b'Advanced')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resources',
            name='link',
            field=models.TextField(),
        ),
    ]
