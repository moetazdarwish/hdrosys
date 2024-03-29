# Generated by Django 4.0 on 2023-02-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0011_alter_pwraction_btn_0_alter_pwraction_btn_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devrecord',
            old_name='button_7',
            new_name='sensor_7',
        ),
        migrations.AlterField(
            model_name='pwraction',
            name='btn_0',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pwraction',
            name='btn_1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pwraction',
            name='btn_2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pwraction',
            name='btn_3',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pwraction',
            name='btn_4',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pwraction',
            name='btn_5',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pwraction',
            name='btn_6',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pwraction',
            name='btn_7',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pwraction',
            name='btn_8',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pwraction',
            name='btn_9',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
