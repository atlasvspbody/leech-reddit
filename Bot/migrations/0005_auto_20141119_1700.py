# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0004_rule_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='regex',
            field=models.CharField(verbose_name='Regex', max_length=100),
            preserve_default=True,
        ),
    ]
