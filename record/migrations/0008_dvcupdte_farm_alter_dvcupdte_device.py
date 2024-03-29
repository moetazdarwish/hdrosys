# Generated by Django 4.0 on 2023-02-19 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0009_alter_frmdevice_type'),
        ('record', '0007_dvcupdte'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvcupdte',
            name='farm',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.frmprofile'),
        ),
        migrations.AlterField(
            model_name='dvcupdte',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.frmdevice'),
        ),
    ]
