# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seatme', '0002_auto_20141214_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='layout',
            field=models.CharField(max_length=1, default='R', choices=[('R', 'Rectangle')]),
            preserve_default=True,
        ),
    ]
