from django.db import models
from Volunteer.models import Volunteer
from Organization.models import Organization

# Create your models here.
class Events(models.Model):

    Event_ID = models.BigAutoField(primary_key=True,unique=True)
    Number_of_Volunteer = models.PositiveIntegerField(verbose_name="Number of Volunteers")
    Size_of_Event = models.PositiveIntegerField(verbose_name="Size of Event")
    Event_Name = models.CharField(max_length=20, verbose_name="Event Name")
    Location = models.CharField(max_length=20, verbose_name="Location")
    Created_Org = models.ForeignKey(Organization, related_name='conducting_Org', on_delete=models.CASCADE)
    Reg_volunteers = models.ManyToManyField(Volunteer, related_name='registered_events', blank=True)

    Event_Date = models.DateTimeField(null = True)
    
    Event_type = [
        ("PAST","Past"),
        ("COMING","Coming")
    ]
    Event_Status =models.CharField(choices = Event_type ,default = "PAST") 
    def __str__(self):
        return self.Event_Name