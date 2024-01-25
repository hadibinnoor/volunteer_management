from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager 
# Create your models here.

class VolunteerManager(BaseUserManager):
    def _create_user(self,email,password,Vol_ID,Name,Gender,Age,Location,**extra_fields):
        email = self.normalize_email(email)
        organization = self.model(
            email = email,
            Vol_ID =Vol_ID,
            Name = Name,
            Age =Age,
            Location = Location
            **extra_fields,
        )
        organization.set_password(password)
        organization.save(using=self._db)
        return organization
    
    def create_user(self, email, password,Vol_ID,Name,Gender,Age,Location, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password,Vol_ID,Name,Gender,Age,Location,**extra_fields)

class volunteer(AbstractBaseUser):
    Gender_type = [
        ("MALE","Male"),
        ("FEMALE","Female"),
        ("OTHERS","Others")
    ]
    email = models.EmailField(unique = True,max_length=254)
    Vol_ID = models.IntegerField(primary_key =True,unique =True)
    Name = models.CharField(max_length=20)
    Gender = models.CharField(choices = Gender_type,max_length=50)
    Age = models.PositiveIntegerField()
    Location = models.CharField(max_length=50)
    
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default = True)
    
    objects = VolunteerManager()
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['Vol_ID','Name','Gender','Age','Location']

    def __str__(self):
        return self.Name


#_________________Organization__________________
    
class Org_Manager(BaseUserManager):
    def _create_user(self,Org_ID,password,Org_Name,Location,verify,**extra_fields):
        organization = self.model(
            Org_ID =Org_ID,
            verify =verify,
            Location = Location,
            **extra_fields,
        )
        organization.set_password(password)
        organization.save(using=self._db)
        return organization
    def create_user(self,Org_ID,password,verify ,Location, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(Org_ID,password,verify,Location,**extra_fields)

    def create_superuser(self, Org_ID, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(Org_ID, password, **extra_fields)

class Org(AbstractBaseUser):
    Org_ID = models.PositiveIntegerField(primary_key=True,unique = True) 
    Org_Name = models.CharField(max_length = 20)
    Location =models.CharField(max_length=50) 
    verify = models.BooleanField(default =False)

    USERNAME_FIELD = 'Org_ID'
    REQUIRED_FIELDS = ['Org_ID','Org_Name','Location','verify']
    objects = Org_Manager()
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default = True)

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
    
    
class Reg_Volunteers(models.Model):
    Volunteer = models.ForeignKey(volunteer, verbose_name=("Record_Volunteer"), on_delete=models.DO_NOTHING)
    Event = models.ForeignKey(Events, verbose_name=("Record_Event"), on_delete=models.CASCADE)
    Register = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.volunteer.Name} Record"