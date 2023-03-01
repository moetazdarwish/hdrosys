# Generated by Django 4.0 on 2023-02-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0013_alter_frmdevice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frmdevice',
            name='attahment',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='frmdevice',
            name='type',
            field=models.CharField(choices=[('MOTION', 'MOTION'), ('CONTROL', 'CONTROL'), ('STATION', 'STATION')], max_length=50),
        ),
    ]
