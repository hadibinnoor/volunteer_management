from django.contrib import admin
from .models import volunteer,Org,Events,Reg_Volunteers
# Register your models here.

admin.site.register(volunteer)
admin.site.register(Org)
admin.site.register(Events)
admin.site.register(Reg_Volunteers)