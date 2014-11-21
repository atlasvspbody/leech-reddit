# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BotFind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateTimeField(verbose_name='Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('selftext', models.TextField(verbose_name='SelfText')),
                ('permalink', models.URLField(verbose_name='Permalink')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuequeAlert',
            fields=[
                ('post_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, primary_key=True, to='Bot.Post')),
            ],
            options={
            },
            bases=('Bot.post',),
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('regex', models.CharField(max_length=50, verbose_name='Regex')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubReddit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('alias', models.CharField(max_length=50, verbose_name='Alias')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='quequealert',
            name='rule',
            field=models.ForeignKey(to='Bot.Rule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='botfind',
            name='subreddit',
            field=models.ForeignKey(to='Bot.SubReddit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alert',
            name='rule',
            field=models.ForeignKey(to='Bot.Rule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alert',
            name='subreddit',
            field=models.ForeignKey(to='Bot.SubReddit'),
            preserve_default=True,
        ),
    ]
