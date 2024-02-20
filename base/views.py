from django.shortcuts import redirect, render
from rest_framework.views import APIView
#models--
from base.models import Events,volunteer,Org
from rest_framework.response import Response
# apiview-
from rest_framework.decorators import api_view
from rest_framework import status
#serilizer---
from base.serializers import EventSerializer,Vols_Serializer,Orgs_serializer
from django.http import HttpResponse
from .forms import EventsForm

# Create your views here.

class CreateEvent(APIView):
    def post(self, request):
        
        try:
            serializer=EventSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer_instance = serializer.save()
                
                serializer_instance.save()
                
                return Response({"event_result": serializer.data}, status=status.HTTP_200_OK)           
            else:
                return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)
            return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
class ImageFile(APIView):
    def get(self,request, pk):
        try:
            image_instance = Events.objects.get(Event_ID=pk)
        except Events.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if image_instance.poster:
            image_path = image_instance.poster.path
            with open(image_path, "rb") as image_file:
                response = HttpResponse(image_file.read(), content_type="image/jpeg")
                response["Content-Disposition"] = f"inline; filename={image_instance.poster.name}"
                return response

        return Response(status=status.HTTP_404_NOT_FOUND)
    
def create_event(request):
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            # Additional processing or redirect
            return redirect('some-success-url')
    else:
        form = EventsForm()
    return render(request, 'form.html', {'form': form})
    
@api_view(['GET'])
def events(request):
    e_obj = Events.objects.all()
    serilizer = EventSerializer(e_obj,many = True) 
    print(serilizer.data)
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



# -----Details of Volunteer ------

@api_view(['GET'])
def Volunteer_details(request,vd):
    vol_obj = volunteer.objects.get(Vol_ID=vd)
    v_serializer = Vols_Serializer(vol_obj,many=False)
    return Response(v_serializer.data)

# -----Details of organization ------

@api_view(['GET'])
def Org_details(request,od):
    Org_obj = Org.objects.get(Org_ID=od)
    or_serializer = Orgs_serializer(Org_obj,many=False)
    return Response(or_serializer.data)

## -----Details of Events ------

@api_view(['GET'])
def event_details(request,ed):
    e_obj = Events.objects.get(Event_ID = ed)
    serilizer = EventSerializer(e_obj,many = False)
    return Response(serilizer.data)