from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
import json
from django.shortcuts import render

# Create your views here.
from farms.frmserializ import LogininSerializer
from farms.models import FrmProfile


@api_view(['POST'])
def loginUser(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        get_user = User.objects.get(username=user)
        token, create = Token.objects.get_or_create(user=get_user)
        try:
            name = FrmProfile.objects.get(farm=get_user)

            key = token.key
            data = {"key": key,
                    "name": name.name,
                    "logo": "none"
                    }
            json_stuff = LogininSerializer(data).data
            return Response(json_stuff)
        except:
            return JsonResponse('Wrong Password ', safe=False)
    else:
        return JsonResponse('Wrong Password or Email', safe=False)