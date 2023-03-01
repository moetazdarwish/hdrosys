from django.db import models

# Create your models here.
from django.db.models.signals import post_save

from farms.models import FrmProfile, FrmDevice


class DevRecord(models.Model):
    device = models.ForeignKey(FrmDevice, on_delete=models.CASCADE)
    sensor_1 = models.FloatField(null=True, blank=True)
    sensor_2 = models.FloatField(null=True, blank=True)
    sensor_3 = models.FloatField(null=True, blank=True)
    sensor_4 = models.FloatField(null=True, blank=True)
    sensor_5 = models.FloatField(null=True, blank=True)
    sensor_6 = models.FloatField(null=True, blank=True)
    sensor_7 = models.FloatField(null=True, blank=True)
    sensor_8 = models.FloatField(null=True, blank=True)
    sensor_9 = models.FloatField(null=True, blank=True)
    sensor_10 = models.FloatField(null=True, blank=True)
    sensor_11 = models.FloatField(null=True, blank=True)
    sensor_12 = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class PwrAction(models.Model):
    device = models.OneToOneField(FrmDevice, on_delete=models.CASCADE)
    btn_0 = models.PositiveIntegerField(null=True, blank=True)
    btn_1 = models.PositiveIntegerField(null=True, blank=True)
    btn_2 = models.PositiveIntegerField(null=True, blank=True)
    btn_3 = models.PositiveIntegerField(null=True, blank=True)
    btn_4 = models.PositiveIntegerField(null=True, blank=True)
    btn_5 = models.PositiveIntegerField(null=True, blank=True)
    btn_6 = models.PositiveIntegerField(null=True, blank=True)
    btn_7 = models.PositiveIntegerField(null=True, blank=True)
    btn_8 = models.PositiveIntegerField(null=True, blank=True)
    btn_9 = models.PositiveIntegerField(null=True, blank=True)
    updte = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


class BtnRecord(models.Model):
    device = models.ForeignKey(FrmDevice, on_delete=models.CASCADE)
    btn_0 = models.PositiveIntegerField(null=True, blank=True, default='0')
    btn_1 = models.PositiveIntegerField(null=True, blank=True, default='0')
    btn_2 = models.PositiveIntegerField(null=True, blank=True, default='0')
    btn_3 = models.PositiveIntegerField(null=True, blank=True, default='0')
    btn_4 = models.PositiveIntegerField(null=True, blank=True, default='0')
    btn_5 = models.PositiveIntegerField(null=True, blank=True, default='0')
    btn_6 = models.PositiveIntegerField(null=True, blank=True, default='0')
    btn_7 = models.PositiveIntegerField(null=True, blank=True, default='0')
    btn_8 = models.PositiveIntegerField(null=True, blank=True, default='0')
    btn_9 = models.PositiveIntegerField(null=True, blank=True, default='0')
    crt_0 = models.FloatField(null=True, blank=True, default='0')
    crt_1 = models.FloatField(null=True, blank=True, default='0')
    crt_2 = models.FloatField(null=True, blank=True, default='0')
    crt_3 = models.FloatField(null=True, blank=True, default='0')
    crt_4 = models.FloatField(null=True, blank=True, default='0')
    crt_5 = models.FloatField(null=True, blank=True, default='0')
    crt_6 = models.FloatField(null=True, blank=True, default='0')
    crt_7 = models.FloatField(null=True, blank=True, default='0')
    crt_8 = models.FloatField(null=True, blank=True, default='0')
    crt_9 = models.FloatField(null=True, blank=True, default='0')
    date = models.DateTimeField(auto_now_add=True)


class DeviceData(models.Model):
    device = models.ForeignKey(FrmDevice, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    re_name = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50)

class PwrBtnNme(models.Model):
    farm = models.ForeignKey(FrmProfile, on_delete=models.CASCADE,null=True, blank=True)
    device = models.OneToOneField(FrmDevice, on_delete=models.CASCADE)
    btn_0 = models.CharField(max_length=50,null=True, blank=True, default='Power 1')
    btn_1 = models.CharField(max_length=50,null=True, blank=True, default='Power 2')
    btn_2 = models.CharField(max_length=50,null=True, blank=True, default='Power 3')
    btn_3 = models.CharField(max_length=50,null=True, blank=True, default='Power 4')
    btn_4 = models.CharField(max_length=50,null=True, blank=True, default='Power 5')
    btn_5 = models.CharField(max_length=50,null=True, blank=True, default='Power 6')
    btn_6 = models.CharField(max_length=50,null=True, blank=True, default='Power 7')
    btn_7 = models.CharField(max_length=50,null=True, blank=True, default='Power 8')
    btn_8 = models.CharField(max_length=50,null=True, blank=True, default='Power 9')
    btn_9 = models.CharField(max_length=50,null=True, blank=True, default='Power 10')

def NwDeviceAdd(sender, instance, created, *args, **kwargs):
    # if created:
    # if instance.type =='STATION':
    #
    #     for i in instance.attahment:
    #         DeviceData.objects.create(device=instance,name="sensor_"+i,re_name="sensor_"+i)
    #         i = +1



    if instance.type == 'CONTROL':
        PwrAction.objects.create(device=instance)
    if instance.type == 'MOTION':
        PwrAction.objects.create(farm=instance.farm, device=instance)


post_save.connect(NwDeviceAdd, sender=FrmDevice)

class DevicesRules(models.Model):
    farm = models.ForeignKey(FrmProfile, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    sdevice = models.ForeignKey(FrmDevice, on_delete=models.CASCADE,related_name='sdevice')
    snsor = models.CharField(max_length=20, null=True, blank=True)
    rulecond = models.CharField(max_length=10, null=True, blank=True)
    snsorvlue = models.CharField(max_length=10, null=True, blank=True)

    cdevice = models.ForeignKey(FrmDevice, on_delete=models.CASCADE, related_name='cdevice')
    btn = models.CharField(max_length=50, null=True, blank=True)
    btntxt = models.CharField(max_length=50, null=True, blank=True)
    btnaction = models.CharField(max_length=50, null=True, blank=True)
    rulstat = models.BooleanField(default=True, null=True, blank=True)


