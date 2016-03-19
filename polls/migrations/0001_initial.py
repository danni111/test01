# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text_unique', models.CharField(max_length=30)),
                ('text_title', models.CharField(max_length=30)),
                ('text_content', models.CharField(max_length=500)),
            ],
        ),
    ]
