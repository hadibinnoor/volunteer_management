from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from base.models import Org,volunteer,User
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


# ----------  vol registration -----------------


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','Role','password']
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):
        # Create user with provided data
        user = User.objects.create_user(**validated_data)
        user.Role = "Vol"
        return user

class VolunteerSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer for creating user
    
    class Meta:
        model = volunteer
        fields = ['user',"Name","Age",'Location', 'Gender']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.Role = "Vol"
        if user_serializer.is_valid():
            # Save the user
            user = user_serializer.save()

            # Create the volunteer associated with the user
            vol = volunteer.objects.create(user=user, **validated_data)
            return vol
        else:
            raise serializers.ValidationError("User data is invalid")


#-----ORg Registration----------
        
    
class OrganizationSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    class Meta:
        model = Org
        fields = ['user',"Org_Name","Location","verified"]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            # Save the user
            user = user_serializer.save()

            org = Org.objects.create(user=user, **validated_data)
            return org
        else:
            raise serializers.ValidationError("User data is invalid")
