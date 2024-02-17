from django.urls import path
from . import views
urlpatterns = [
    path('Events/',views.events),
    path('Volunteers/',views.Volunteers),
    path('orgs/',views.oranizations),

    
]