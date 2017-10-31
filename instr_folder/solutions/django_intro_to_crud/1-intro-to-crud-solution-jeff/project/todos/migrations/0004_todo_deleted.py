# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20160519_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
