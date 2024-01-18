from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class OrganizationManager(BaseUserManager):
    def create_organization(self, Org_ID, Org_Name, Location_of, password=None, **extra_fields):
        organization = self.model(
            Org_ID=Org_ID,
            Org_Name=Org_Name,
            Location_of=Location_of,
            **extra_fields
        )
        organization.set_password(password)
        organization.save(using=self._db)
        return organization

class Organization(AbstractBaseUser):
    Org_ID = models.BigAutoField(primary_key=True,unique = True)
    Org_Name = models.CharField(max_length = 20)
    Location_of =models.CharField(max_length=50) 
    verify = models.BooleanField(default =False)
    
    objects = OrganizationManager()

    USERNAME_FIELD = 'Org_ID'
    REQUIRED_FIELDS = ['Org_Name','Location_of','Verify']

    def __str__(self):
        return self.Org_Name

