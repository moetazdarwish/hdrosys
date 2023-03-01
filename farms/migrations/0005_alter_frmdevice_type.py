# Generated by Django 4.0 on 2023-02-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0004_frmdevice_name_alter_frmdevice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frmdevice',
            name='type',
            field=models.CharField(choices=[('MOTION', 'MOTION'), ('STATION', 'STATION'), ('POWER', 'POWER')], max_length=50),
        ),
    ]
