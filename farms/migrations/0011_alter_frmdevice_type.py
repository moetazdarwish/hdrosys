# Generated by Django 4.0 on 2023-02-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0010_frmdevice_attahment_alter_frmdevice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frmdevice',
            name='type',
            field=models.CharField(choices=[('CONTROL', 'CONTROL'), ('MOTION', 'MOTION'), ('STATION', 'STATION')], max_length=50),
        ),
    ]
