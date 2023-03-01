# Generated by Django 4.0 on 2023-02-24 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0016_alter_frmdevice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frmdevice',
            name='type',
            field=models.CharField(choices=[('STATION', 'STATION'), ('CONTROL', 'CONTROL'), ('MOTION', 'MOTION')], max_length=50),
        ),
    ]
