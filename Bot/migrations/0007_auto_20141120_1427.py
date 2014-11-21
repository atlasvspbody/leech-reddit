# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0006_alert_alias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='subreddit',
            name='alias',
        ),
    ]
