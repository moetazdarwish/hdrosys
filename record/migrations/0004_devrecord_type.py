# Generated by Django 4.0 on 2023-02-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_rename_amp_devrecord_amp_0_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='devrecord',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
