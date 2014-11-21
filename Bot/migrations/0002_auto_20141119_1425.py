# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subreddit',
            name='alias',
            field=models.CharField(verbose_name='Alias', blank=True, max_length=50),
            preserve_default=True,
        ),
    ]
