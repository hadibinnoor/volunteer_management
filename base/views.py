from django.shortcuts import render
from rest_framework.response import Response

#models--
from base.models import Events,volunteer,Org

# apiview-
from rest_framework.decorators import api_view

#serilizer---
from base.serializers import EventSerializer,Vols_Serializer,Orgs_serializer

# Create your views here.



@api_view(['GET'])
def events(request):
    e_obj = Events.objects.all()
    serilizer = EventSerializer(e_obj,many = True)
    return Response(serilizer.data)


@api_view(['GET'])
def Volunteers(request):
    vol_obj = volunteer.objects.all()
    v_serializer = Vols_Serializer(vol_obj,many=True)
    return Response(v_serializer.data)


@api_view(['GET'])
def oranizations(request):
    Org_obj = Org.objects.all()
    or_serializer = Orgs_serializer(Org_obj,many=True)
    return Response(or_serializer.data)