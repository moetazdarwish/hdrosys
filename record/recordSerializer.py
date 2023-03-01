from rest_framework import serializers
from .models import *



class PwrActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PwrAction
        fields =  ["btn_0","btn_1","btn_2","btn_3","btn_4","btn_5","btn_6","btn_7","btn_8","btn_9"]


class MtnActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PwrAction
        fields = "__all__"



class DisplaySenrRecord(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = DevRecord
        fields = "__all__"

class DisplaylatestRecord(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField('get_detail')
    class Meta:
        model = FrmDevice
        fields = ["id","name","device","attahment","type","detail"]

    def get_detail(self, obj):
        get_dta = DevRecord.objects.filter(device=obj).last()
        data = DisplaySenrRecord(get_dta).data
        return data
class GetSensorsserializer(serializers.ModelSerializer):

    class Meta:
        model = FrmDevice
        fields = ["id","name","device","attahment","type"]


### Control

class DisplayControlRecord(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    data = serializers.SerializerMethodField('get_data')
    class Meta:
        model = BtnRecord
        fields = ['id','data','date' ]

    def get_data(self, obj):
        key_id = self.context.get("ky")
        if key_id == 'btn_0':

            return {
                'btn':obj.btn_0,
                'crt':obj.crt_0
            }
        if key_id == 'btn_1':
            return {
                'btn':obj.btn_1,
                'crt':obj.crt_1
            }
        if key_id == 'btn_2':
            return {
                'btn':obj.btn_2,
                'crt':obj.crt_2
            }
        if key_id == 'btn_3':
            return {
                'btn':obj.btn_3,
                'crt':obj.crt_3
            }
        if key_id == 'btn_4':
            return {
                'btn':obj.btn_4,
                'crt':obj.crt_4
            }
        if key_id == 'btn_5':
            return {
                'btn':obj.btn_5,
                'crt':obj.crt_5
            }
        if key_id == 'btn_6':
            return {
                'btn':obj.btn_6,
                'crt':obj.crt_6
            }
        if key_id == 'btn_7':
            return {
                'btn':obj.btn_7,
                'crt':obj.crt_7
            }
        if key_id == 'btn_8':
            return {
                'btn':obj.btn_8,
                'crt':obj.crt_8
            }
        if key_id == 'btn_9':
            return {
                'btn':obj.btn_9,
                'crt':obj.crt_9
            }


class DisplayBtnRecord(serializers.ModelSerializer):

    class Meta:
        model = BtnRecord
        fields = ['btn_0' ,'btn_1' ,'btn_2' ,'btn_3' ,'btn_4' ,'btn_5' ,'btn_6' ,'btn_7' ,'btn_8','btn_9' ]
class DisplayCrtRecord(serializers.ModelSerializer):

    class Meta:
        model = BtnRecord
        fields = ['crt_0' ,'crt_1' ,'crt_2' ,'crt_3' ,'crt_4' ,'crt_5' ,'crt_6' ,'crt_7' ,'crt_8','crt_9' ]
class DisplayRecordDetails(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = BtnRecord
        fields = ['device','date' ]

class DisplayNmeRecord(serializers.ModelSerializer):

    class Meta:
        model = PwrBtnNme
        fields = ['btn_0' ,'btn_1' ,'btn_2' ,'btn_3' ,'btn_4' ,'btn_5' ,'btn_6' ,'btn_7' ,'btn_8','btn_9' ]

class DisplaylatestControlRecord(serializers.ModelSerializer):
    btn = serializers.SerializerMethodField('get_btn')
    crt = serializers.SerializerMethodField('get_crt')
    name = serializers.SerializerMethodField('get_name')
    data = serializers.SerializerMethodField('get_data')

    class Meta:
        model = PwrBtnNme
        fields = ['btn','crt','name','data']

    def get_btn(self, obj):
        get_dta = BtnRecord.objects.filter(device=obj.device).last()
        data = DisplayBtnRecord(get_dta).data
        return data
    def get_crt(self, obj):
        get_dta = BtnRecord.objects.filter(device=obj.device).last()
        data = DisplayCrtRecord(get_dta).data
        return data
    def get_data(self, obj):
        get_dta = BtnRecord.objects.filter(device=obj.device).last()
        data = DisplayRecordDetails(get_dta).data
        return data
    def get_name(self, obj):
        get_dta = PwrBtnNme.objects.get(id=obj.id)
        data = DisplayNmeRecord(get_dta).data
        return data

class DisplayRulsNme(serializers.ModelSerializer):
    btn = serializers.SerializerMethodField('get_btn')
    class Meta:
        model = PwrBtnNme
        fields = ['device','btn']

    def get_btn(self, obj):
        data = DisplayNmeRecord(obj).data
        return data

class GetRulesSerial(serializers.ModelSerializer):

    class Meta:
        model = DevicesRules
        fields = "__all__"

