from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

"""class VolunteerManager(BaseUserManager):
    def create_volunteer(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_volunteer', True)
        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
"""

class Volunteer(models.Model):
    Gender_Type = [
        ("MALE","Male"),
        ("FEMALE","Female"),
        ("OTHERS","Others"),
    ]
    email = models.EmailField(unique=True) # --login( username )--
    is_volunteer = models.BooleanField(default=True) 
    Volunteer_ID = models.IntegerField(primary_key=True,unique = True)
    Name = models.CharField(max_length=20)
    Gender = models.CharField(max_length=6,choices = Gender_Type)
    Age = models.IntegerField()
    Location = models.CharField(max_length=20)

    def __str__(self):
        return self.Name




