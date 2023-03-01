# Generated by Django 4.0 on 2023-03-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0022_alter_frmdevice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frmdevice',
            name='type',
            field=models.CharField(choices=[('MOTION', 'MOTION'), ('CONTROL', 'CONTROL'), ('STATION', 'STATION')], max_length=50),
        ),
    ]
