# Generated by Django 4.0 on 2023-03-01 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0018_alter_frmdevice_type'),
        ('record', '0016_pwrbtnnme_farm'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevicesRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('snsor', models.CharField(blank=True, max_length=20, null=True)),
                ('snsorvlue', models.CharField(blank=True, max_length=5, null=True)),
                ('rulecond', models.CharField(blank=True, max_length=5, null=True)),
                ('btn', models.CharField(blank=True, max_length=50, null=True)),
                ('btnaction', models.CharField(blank=True, max_length=50, null=True)),
                ('rulstat', models.CharField(blank=True, max_length=50, null=True)),
                ('cdevice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cdevice', to='farms.frmdevice')),
                ('sdevice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sdevice', to='farms.frmdevice')),
            ],
        ),
    ]
