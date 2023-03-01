

from django.urls import path, include
from . import views

urlpatterns = [
    path('addRecord/', views.addRecord, name="addRecord"),
    path('addRecordtst/', views.addRecordtst, name="addRecordtst"),
    path('getButonSte/', views.getButonSte, name="getButonSte"),
    path('dtarcivertst/', views.dtarcivertst, name="dtarcivertst"),
    path('dtasenttst/', views.dtasenttst, name="dtasenttst"),
    path('mainRead/', views.mainRead, name="mainRead"),
    path('getSnsors/', views.getSnsors, name="getSnsors"),
    path('getSnsorsRecord/', views.getSnsorsRecord, name="getSnsorsRecord"),
    path('renameSensor/', views.renameSensor, name="renameSensor"),
    path('mainControl/', views.mainControl, name="mainControl"),
    path('keyControlUpdate/', views.keyControlUpdate, name="keyControlUpdate"),
    path('keyControlRename/', views.keyControlRename, name="keyControlRename"),
    path('getPwrRecord/', views.getPwrRecord, name="getPwrRecord"),
    path('rulsGetPwr/', views.rulsGetPwr, name="rulsGetPwr"),
    path('creatRules/', views.creatRules, name="creatRules"),
    path('getFarmRules/', views.getFarmRules, name="getFarmRules"),
    path('rulesStatChnge/', views.rulesStatChnge, name="rulesStatChnge"),

]
