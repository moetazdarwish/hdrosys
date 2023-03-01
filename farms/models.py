from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token
# Create your models here.
from django.db.models.signals import post_save
DEVICE_TYPS = {
    ('STATION','STATION'),
    ('CONTROL' ,'CONTROL'),
    ('MOTION','MOTION')
}

class FrmProfile(models.Model):
    farm = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    location = models.TextField(null=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FrmDevice(models.Model):
    farm = models.ForeignKey(FrmProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True,blank=True)
    device = models.CharField(max_length=50)
    attahment = models.PositiveIntegerField(null=True,blank=True)
    type = models.CharField(max_length=50,choices=DEVICE_TYPS)
    def __str__(self):
        return self.name











def Tokencreatoruser(sender, instance, created, *args, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)


post_save.connect(Tokencreatoruser, sender=User)
