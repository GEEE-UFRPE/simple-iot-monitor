# Generated by Django 3.0.1 on 2020-07-20 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iotmonitor', '0007_auto_20200716_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='name',
            new_name='thing_monitored',
        ),
    ]
