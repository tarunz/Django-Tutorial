# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ctext', models.CharField(max_length=250)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qtext', models.CharField(max_length=250)),
                ('pdate', models.DateTimeField(verbose_name=b'Date Published')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='Q',
            field=models.ForeignKey(to='polls.Question'),
        ),
    ]
