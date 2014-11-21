# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0002_auto_20141119_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subreddit',
            name='alias',
            field=models.CharField(blank=True, null=True, default=None, max_length=50, verbose_name='Alias'),
            preserve_default=True,
        ),
    ]
