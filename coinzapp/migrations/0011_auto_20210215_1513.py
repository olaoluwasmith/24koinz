# Generated by Django 3.1.6 on 2021-02-15 14:13

import coinzapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinzapp', '0010_auto_20210215_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='vendor_id',
            field=models.CharField(blank=True, default=coinzapp.models.f, editable=False, max_length=15, unique=True),
        ),
    ]
