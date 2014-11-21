# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0003_auto_20141119_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='alias',
            field=models.CharField(default=None, blank=True, max_length=50, verbose_name='Alias', null=True),
            preserve_default=True,
        ),
    ]
