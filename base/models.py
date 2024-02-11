from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager 
# Create your models here.

class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True)
    user_type = (
        ("Org","organization"),
        ("Vol","volunteer")
    )
    Role = models.CharField(choices = user_type, max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Role']

    def __str__(self):
        return self.email
    


class volunteer(models.Model):
    Gender_type = [
        ("MALE","Male"),
        ("FEMALE","Female"),
        ("OTHERS","Others")
    ]
    user = models.OneToOneField(User, related_name ="vol_profile",on_delete=models.CASCADE)
    Vol_ID = models.IntegerField(primary_key =True,unique =True)
    Name = models.CharField(max_length=20)
    Gender = models.CharField(choices = Gender_type,max_length=50)
    Age = models.PositiveIntegerField()
    Location = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

#_________________Organization__________________
    

class Org(models.Model):
    user =models.OneToOneField(User, related_name = "org_profile", on_delete=models.CASCADE)
    Org_ID = models.PositiveIntegerField(primary_key=True,unique = True) 
    Org_Name = models.CharField(max_length = 20)
    Location =models.CharField(max_length=50) 
    verify = models.BooleanField(default =False)

    def __str__(self):
        return self.Org_Name
    

#____________Events__________________________________

class Events(models.Model):

    Event_ID = models.BigAutoField(primary_key=True,unique=True)
    Number_of_Volunteer = models.PositiveIntegerField(verbose_name="Number of Volunteers")
    Size_of_Event = models.PositiveIntegerField(verbose_name="Size of Event")
    Event_Name = models.CharField(max_length=20, verbose_name="Event Name")
    Location = models.CharField(max_length=20, verbose_name="Location")
    Created_Org = models.ForeignKey(Org, related_name='conducting_Org', on_delete=models.CASCADE) # conducting organization

    Event_Date = models.DateTimeField(null = True)
    
    Event_type = [
        ("PAST","Past"),
        ("COMING","Coming")
    ]
    Event_Status =models.CharField(choices = Event_type ,default = "COMING",max_length = 20) 
    def __str__(self):
        return self.Event_Name
    
    
class registered(models.Model):
    vol = models.ForeignKey(volunteer, related_name = "reg_vol", on_delete=models.CASCADE)
    event = models.ForeignKey(Events, related_name = "event", on_delete=models.CASCADE)

    def __str__(*self):
        return f"ff"