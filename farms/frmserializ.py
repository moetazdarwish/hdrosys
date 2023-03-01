from rest_framework import serializers
from .models import *


class LogininSerializer(serializers.Serializer):
    key = serializers.CharField()
    name = serializers.CharField()
    logo = serializers.CharField()