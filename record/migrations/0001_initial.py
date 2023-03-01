# Generated by Django 4.0 on 2023-02-01 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farms', '0002_alter_frmdevice_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.FloatField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.frmdevice')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.frmprofile')),
            ],
        ),
    ]