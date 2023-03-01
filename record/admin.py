from django.contrib import admin

# Register your models here.
from record.models import *

admin.site.register(DevRecord)
admin.site.register(PwrAction)
admin.site.register(BtnRecord)
admin.site.register(PwrBtnNme)
admin.site.register(DevicesRules)
