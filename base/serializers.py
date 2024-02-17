from rest_framework.serializers import ModelSerializer

#models --
from base.models import Events,volunteer,Org

class EventSerializer(ModelSerializer):
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