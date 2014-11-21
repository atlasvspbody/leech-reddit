# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0005_auto_20141119_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='alias',
            field=models.CharField(default=None, verbose_name='Alias', blank=True, max_length=50, null=True),
            preserve_default=True,
        ),
    ]
