# Generated by Django 4.0 on 2023-02-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devrecord',
            old_name='reading',
            new_name='amp',
        ),
        migrations.RenameField(
            model_name='devrecord',
            old_name='status',
            new_name='button',
        ),
        migrations.AddField(
            model_name='devrecord',
            name='humd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devrecord',
            name='light',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devrecord',
            name='motion',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devrecord',
            name='temp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devrecord',
            name='temp2',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
