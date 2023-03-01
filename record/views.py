import json

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from farms.models import FrmProfile, FrmDevice
from record.models import DevRecord, PwrAction
from record.recordSerializer import *


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def addRecord(request):
    type = request.POST.get('type')
    device = request.POST.get('device')
    if type == 'ST':
        temp = request.POST.get('temp')
        hum = request.POST.get('hum')
        temp_1 = request.POST.get('temp_1')
        light = request.POST.get('light')
        get_dvce = FrmDevice.objects.get(device=device)
        DevRecord.objects.create(farm=get_dvce.farm, device=get_dvce, temp=temp, humd=hum, light=light, temp2=temp_1)
        return Response(status=200)
    if type == 'PWR':
        button_0 = request.POST.get('button_0')
        amp_0 = request.POST.get('amp_0')
        button_1 = request.POST.get('button_0')
        amp_1 = request.POST.get('amp_0')
        button_2 = request.POST.get('button_0')
        amp_2 = request.POST.get('amp_0')
        button_3 = request.POST.get('button_0')
        amp_3 = request.POST.get('amp_0')
        button_4 = request.POST.get('button_0')
        amp_4 = request.POST.get('amp_0')
        button_5 = request.POST.get('button_0')
        amp_5 = request.POST.get('amp_0')
        button_6 = request.POST.get('button_0')
        amp_6 = request.POST.get('amp_0')
        button_7 = request.POST.get('button_0')
        amp_7 = request.POST.get('amp_0')
        button_8 = request.POST.get('button_0')
        amp_8 = request.POST.get('amp_0')
        button_9 = request.POST.get('button_0')
        amp_9 = request.POST.get('amp_0')
        get_dvce = FrmDevice.objects.get(device=device)
        DevRecord.objects.create(farm=get_dvce.farm, device=get_dvce,
                                 button_0=button_0, amp_0=amp_0, button_1=button_1, amp_1=amp_1,
                                 button_2=button_2, amp_2=amp_2, button_3=button_3, amp_3=amp_3,
                                 button_4=button_4, amp_4=amp_4, button_5=button_5, amp_5=amp_5,
                                 button_6=button_6, amp_6=amp_6, button_7=button_7, amp_7=amp_7,
                                 button_8=button_8, amp_8=amp_8, button_9=button_9, amp_9=amp_9,
                                 )
        get_action = PwrAction.objects.get(device=get_dvce)
        data = {}
        if get_action:
            data = PwrActionSerializer(get_action).data
        return Response(data)
    if type == 'MTN':
        motion = request.POST.get('motion')
        get_dvce = FrmDevice.objects.get(device=device)
        DevRecord.objects.create(farm=get_dvce.farm, device=get_dvce,
                                 motion=motion)
        get_action = PwrAction.objects.get(device=get_dvce)
        if get_action.motion == 1:
            data = {
                "motion": 0
            }
            return Response(data)
        else:
            data = {
                "motion": motion
            }
            return Response(data)


@api_view(['POST'])
def addRecordtst(request):
    print(request.body)
    s_mode = request.POST.get('type')
    device = request.POST.get('device')
    if s_mode == 'ST':
        temp = request.POST.get('temp')
        hum = request.POST.get('hum')
        temp_1 = request.POST.get('temp_1')
        light = request.POST.get('light')
        get_dvce = FrmDevice.objects.get(device=device)
        DevRecord.objects.create(device=get_dvce, sensor_1=temp, sensor_2=hum, sensor_3=light, sensor_4=temp_1)
        return Response(status=200)
    if s_mode == 'PR':
        sensor_1 = request.POST.get('s1')
        sensor_2 = request.POST.get('s2')
        sensor_3 = request.POST.get('s3')
        sensor_4 = request.POST.get('s4')
        sensor_5 = request.POST.get('s5')
        sensor_6 = request.POST.get('s6')
        button_7 = request.POST.get('s7')
        sensor_8 = request.POST.get('s8')
        sensor_9 = request.POST.get('s9')
        sensor_10 = request.POST.get('s10')
        sensor_11 = request.POST.get('s11')
        sensor_12 = request.POST.get('s12')
        get_dvce = FrmDevice.objects.get(device=device)
        DevRecord.objects.create(device=get_dvce, sensor_1=sensor_1, sensor_2=sensor_2, sensor_3=sensor_3,
                                 sensor_4=sensor_4, sensor_5=sensor_5, sensor_6=sensor_6, button_7=button_7,
                                 sensor_8=sensor_8, sensor_9=sensor_9, sensor_10=sensor_10, sensor_11=sensor_11
                                 , sensor_12=sensor_12)
        return Response(status=200)
    return Response(status=200)


@api_view(['POST'])
def getButonSte(request):
    device = request.POST.get('device')
    get_dvce = FrmDevice.objects.get(device=device)
    try:
        get_action = PwrAction.objects.get(device=get_dvce, updte=True)
        newdata = {}
        get_action.updte = False
        get_action.save()
        BtnRecord.objects.create(device=get_dvce,btn_0=get_action.btn_0,btn_1=get_action.btn_1
                                         ,btn_2=get_action.btn_2,btn_3=get_action.btn_3,btn_4=get_action.btn_4
                                         ,btn_5=get_action.btn_5,btn_6=get_action.btn_6,btn_7=get_action.btn_7
                                         ,btn_8=get_action.btn_8,btn_9=get_action.btn_9)

        if get_action:
            data = PwrActionSerializer(get_action).data
            for k, v in data.items():
                if v != None:
                    newdata[k] = v

        return Response(newdata)
    except:
        return Response("False")


@api_view(['POST'])
def dtarcivertst(request):
    print(request.body)
    return Response(status=200)


@api_view(['POST'])
def dtasenttst(request):
    print(request.body)
    data = {
        "button_0": "0",
        "button_1": "1",
        "button_2": "1",
        "button_3": "1",
        "button_4": "1",
        "button_5": "1",
        "button_6": "1",
        "button_7": "1",
        "button_8": "0",
    }
    json_object = json.dumps(data)
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def mainRead(request):
    get_frm = FrmProfile.objects.get(farm=request.user)
    get_device = FrmDevice.objects.filter(farm=get_frm, type='STATION')
    data = {}

    if get_device:
        data = DisplaylatestRecord(get_device, many=True).data

    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def getSnsors(request):
    get_frm = FrmProfile.objects.get(farm=request.user)
    get_device = FrmDevice.objects.filter(farm=get_frm, type='STATION')
    data = {}

    if get_device:
        data = GetSensorsserializer(get_device, many=True).data

    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def getSnsorsRecord(request):
    device = request.POST.get('device')
    get_devic = FrmDevice.objects.get(id=device)
    get_recd = DevRecord.objects.filter(device=get_devic)
    data = {}

    if get_recd:
        data = DisplaySenrRecord(get_recd, many=True).data
    return Response(data)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def renameSensor(request):
    device = request.POST.get('device')
    new_name = request.POST.get('re_name')
    print(new_name)
    get_devic = FrmDevice.objects.get(id=device)
    get_devic.name = new_name
    get_devic.save()

    return Response(status=200)

### Control
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def mainControl(request):
    get_frm = FrmProfile.objects.get(farm=request.user)
    get_device = PwrBtnNme.objects.filter(farm=get_frm)
    data = {}
    newdata=[]
    btn=[]
    crt=[]
    name=[]
    if get_device:
        data = DisplaylatestControlRecord(get_device, many=True).data
        for i in data:
            for m,v in i['btn'].items():
                object = {
                    'btn':v,
                    'btnme':m,
                }
                btn.append(object)
            for m,v in i['crt'].items():
                object = {
                    'crt':v,
                }
                crt.append(object)
            for m,v in i['name'].items():
                object = {
                    'name':v,
                }
                name.append(object)
            for b,c,n in zip(btn,crt,name):

                object = {
                    'btn': b['btn'],
                    'btnme': b['btnme'],
                    'crt': c['crt'],
                    'name': n['name'],
                    'device': i['data']['device'],
                    'date': i['data']['date'],
                }
                newdata.append(object)
    return Response(newdata)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def keyControlUpdate(request):
    device = request.POST.get('device')
    kyname = request.POST.get('btnme')
    print(kyname)
    kyvalue = request.POST.get('value')
    print(kyvalue)
    get_frm = FrmDevice.objects.get(id=device)
    get_device = PwrAction.objects.get(device=get_frm)
    if kyname == 'btn_0':
        get_device.btn_0=kyvalue
        get_device.updte=True
        get_device.save()
    if kyname == 'btn_1':
        get_device.btn_1=kyvalue
        get_device.updte = True
        get_device.save()
    if kyname == 'btn_2':
        get_device.btn_2=kyvalue
        get_device.updte = True
        get_device.save()
    if kyname == 'btn_3':
        get_device.btn_3 = kyvalue
        get_device.updte = True
        get_device.save()
    if kyname == 'btn_4':
        get_device.btn_4 = kyvalue
        get_device.updte = True
        get_device.save()
    if kyname == 'btn_5':
        get_device.btn_5 = kyvalue
        get_device.updte = True
        get_device.save()
    if kyname == 'btn_6':
        get_device.btn_6 = kyvalue
        get_device.updte = True
        get_device.save()
    if kyname == 'btn_7':
        get_device.btn_7 = kyvalue
        get_device.updte = True
        get_device.save()
    if kyname == 'btn_8':
        get_device.btn_8 = kyvalue
        get_device.updte = True
        get_device.save()
    if kyname == 'btn_9':
        get_device.btn_9 = kyvalue
        get_device.updte = True
        get_device.save()

    return Response(status=200)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def keyControlRename(request):
    device = request.POST.get('device')
    kyname = request.POST.get('btnme')
    kyvalue = request.POST.get('rename')
    get_frm = FrmDevice.objects.get(id=device)
    get_device = PwrBtnNme.objects.get(device=get_frm)
    if kyname == 'btn_0':
        get_device.btn_0=kyvalue
        get_device.save()
    if kyname == 'btn_1':
        get_device.btn_1=kyvalue
        get_device.save()
    if kyname == 'btn_2':
        get_device.btn_2=kyvalue
        get_device.save()
    if kyname == 'btn_3':
        get_device.btn_3 = kyvalue
        get_device.save()
    if kyname == 'btn_4':
        get_device.btn_4 = kyvalue
        get_device.save()
    if kyname == 'btn_5':
        get_device.btn_5 = kyvalue
        get_device.save()
    if kyname == 'btn_6':
        get_device.btn_6 = kyvalue
        get_device.save()
    if kyname == 'btn_7':
        get_device.btn_7 = kyvalue
        get_device.save()
    if kyname == 'btn_8':
        get_device.btn_8 = kyvalue
        get_device.save()
    if kyname == 'btn_9':
        get_device.btn_9 = kyvalue
        get_device.save()

    return Response(status=200)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def getPwrRecord(request):
    device = request.POST.get('device')
    kyname = request.POST.get('btnme')
    get_devic = FrmDevice.objects.get(id=device)
    get_recd = BtnRecord.objects.filter(device=get_devic)
    data = {}
    if get_recd:
        data = DisplayControlRecord(get_recd, many=True,context={'ky':kyname}).data
    return Response(data)


#### Rules

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def rulsGetPwr(request):
    get_frm = FrmProfile.objects.get(farm=request.user)
    get_device = PwrBtnNme.objects.filter(farm=get_frm)
    data = {}
    newdata=[]
    if get_device:
        data = DisplayRulsNme(get_device, many=True).data
        for i in data:
            for m,v in i['btn'].items():
                object = {
                    'btn': v,
                    'btnme': m,
                    'device': i['device'],
                }
                newdata.append(object)

    return Response(newdata)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def creatRules(request):
    get_frm = FrmProfile.objects.get(farm=request.user)
    device = request.POST.get('device')
    rl_name = request.POST.get('rl_name')
    rl_value = request.POST.get('rl_value')
    rl_con = request.POST.get('rl_con')
    rl_action = request.POST.get('rl_action')
    rl_sensor = request.POST.get('rl_sensor')
    rl_btn = request.POST.get('rl_btn')
    redcond = request.POST.get('redcond')
    btntxt = request.POST.get('btntxt')
    cdevice=FrmDevice.objects.get(id=device)
    sdevice=FrmDevice.objects.get(id=rl_sensor)
    DevicesRules.objects.create(farm=get_frm,name=rl_name,sdevice=sdevice,snsor=redcond,snsorvlue=rl_value,
                                          rulecond=rl_con,cdevice=cdevice,btn=rl_btn,btnaction=rl_action,
                                          btntxt=btntxt)

    return Response(status=200)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def getFarmRules(request):
    get_frm = FrmProfile.objects.get(farm=request.user)

    get_rules =DevicesRules.objects.filter(farm=get_frm)

    data = {}

    if get_rules:
        data = GetRulesSerial(get_rules, many=True).data

    return Response(data)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def rulesStatChnge(request):
    device = request.POST.get('device')
    vle = request.POST.get('value')
    print(vle)


    get_rules =DevicesRules.objects.get(id=device)
    get_rules.rulstat = vle
    get_rules.save()
    return Response(status=200)

