# Generated by Django 3.0.2 on 2020-07-16 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iotmonitor', '0004_auto_20200716_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thing',
            old_name='name_of_type',
            new_name='type',
        ),
    ]
