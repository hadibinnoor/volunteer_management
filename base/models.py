from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.
import os

class CustomUserManager(BaseUserManager):
    def create_user(self, email, Role, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, Role=Role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, Role, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, Role, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    user_type = (
        ("Org","organization"),
        ("Vol","volunteer")
    )
    Role = models.CharField(choices = user_type, max_length=50)
    
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Role']
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return self.email
    


class volunteer(models.Model):
    Gender_type = [
        ("MALE","Male"),
        ("FEMALE","Female"),
        ("OTHERS","Others")
    ]
    user = models.OneToOneField(User, related_name ="vol_profile",on_delete=models.CASCADE)
    Vol_ID = models.BigAutoField(primary_key=True,unique=True)
    Name = models.CharField(max_length=20,default = "empty")
    Gender = models.CharField(choices = Gender_type,max_length=50)
    Age = models.PositiveIntegerField(default = 00)
    Location = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='vol_profile/', null=True, blank=True)

    def __str__(self):
        return self.Name

#_________________Organization__________________
    

class Org(models.Model):
    user =models.OneToOneField(User, related_name = "org_profile", on_delete=models.CASCADE)
    Org_ID = models.BigAutoField(primary_key=True,unique=True)
    Org_Name = models.CharField(max_length = 20)
    Location =models.CharField(max_length=50) 
    verified = models.BooleanField(default =False)

    def __str__(self):
        return self.Org_Name
    

#____________Events__________________________________

class Events(models.Model):

    Event_ID = models.BigAutoField(primary_key=True,unique=True,)
    Event_Description = models.TextField()
    Number_of_Volunteer = models.PositiveIntegerField(verbose_name="Number of Volunteers")
    Size_of_Event = models.PositiveIntegerField(verbose_name="Size of Event")
    Event_Name = models.CharField(max_length=20, verbose_name="Event Name")
    Location = models.CharField(max_length=20, verbose_name="Location")
    poster = models.ImageField(upload_to='posters/',null=True,blank=True)
    Created_Org = models.ForeignKey(Org, related_name='conducting_Org', on_delete=models.CASCADE) # conducting organization
    Registration_option = models.BooleanField(default = True)
    poster_url = models.TextField(blank=True,null=True)
    Event_Date = models.DateTimeField(null = True,blank = True)
    
    Event_type = [
        ("PAST","Past"),
        ("COMING","Coming")
    ]
    Event_Status =models.CharField(choices = Event_type ,default = "COMING",max_length = 20) 

    #To Get Org_Name---
    def get_Org_Name(self):
        return self.Created_Org.Org_Name

    def __str__(self):
        return self.Event_Name
    
    def save(self, *args, **kwargs):
        # Remove the if condition checking for self.Event_ID
        print(self.Event_ID)
        existing_instance = None
        if self.pk:  # Check if the instance has already been saved
            existing_instance = Events.objects.get(pk=self.pk)
           
            if existing_instance.poster != self.poster:
                # Delete the old image file
                if existing_instance.poster:
                    path = existing_instance.poster.path
                    if os.path.isfile(path):
                        os.remove(path)

        if self.poster:
            self.poster_url = f"poster/media/{self.pk}/file/"

        super().save(*args, **kwargs)
class registered(models.Model):
    vol = models.ForeignKey(volunteer, related_name = "reg_vol", on_delete=models.CASCADE)
    event = models.ForeignKey(Events, related_name = "event", on_delete=models.CASCADE)

    def __str__(*self):
        return f"Reg_member"