# Generated by Django 3.1.6 on 2021-02-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinzapp', '0003_profile_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Status'},
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='number_of_refferral',
            new_name='number_of_referral',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='refferal_bonus',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='refferral_id',
        ),
        migrations.AddField(
            model_name='detail',
            name='referral_bonus',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='referral_id',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
