# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoTextMap',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('PhotoTextMap_texttitle', models.CharField(max_length=30)),
                ('PhotoTextMap_phototype', models.CharField(max_length=30)),
                ('PhotoTextMap_phototitle', models.CharField(max_length=30)),
            ],
        ),
    ]
