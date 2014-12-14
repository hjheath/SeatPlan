# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seatme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='male',
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Not Specified')], max_length=1, default='U'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='enemies',
            field=models.ManyToManyField(related_name='enemies_rel_+', to='seatme.Person', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to='seatme.Person', null=True, blank=True),
            preserve_default=True,
        ),
    ]
