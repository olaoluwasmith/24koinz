# Generated by Django 3.1.6 on 2021-02-14 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, default='', max_length=200)),
                ('refferral_id', models.CharField(blank=True, default='', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(blank=True, default=0, max_length=50, null=True)),
                ('refferal_bonus', models.IntegerField(blank=True, default=0, max_length=50, null=True)),
                ('total_balance', models.IntegerField(blank=True, default=0, max_length=50, null=True)),
                ('number_of_refferral', models.IntegerField(blank=True, default=0, max_length=50, null=True)),
                ('coupon', models.CharField(blank=True, max_length=50)),
                ('vendor_id', models.CharField(blank=True, max_length=50)),
                ('current_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coinzapp.package')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coinzapp.status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]