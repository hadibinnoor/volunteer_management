from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from base.models import Org

#models --
from base.models import Events,volunteer,Org

class EventSerializer(ModelSerializer):
    Org_Name = serializers.CharField(source='Created_Org.Org_Name')
    class Meta:
        model = Events
        fields = '__all__'


class Vols_Serializer(ModelSerializer):
    class Meta:
        model = volunteer
        fields = '__all__'


class Orgs_serializer(ModelSerializer):
    class Meta:
        model = Org
        fields = '__all__'