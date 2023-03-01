from django.contrib import admin

# Register your models here.
from farms.models import *

admin.site.register(FrmProfile)
admin.site.register(FrmDevice)