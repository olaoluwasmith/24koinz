# Generated by Django 3.1.6 on 2021-02-14 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinzapp', '0002_auto_20210214_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
