from django.contrib import admin
from .models import volunteer,Org,Events,User,registered
# Register your models here.

admin.site.register(volunteer)
admin.site.register(Org)
admin.site.register(Events)
admin.site.register(User)
admin.site.register(registered)