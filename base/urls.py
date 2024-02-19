from django.urls import path
from . import views
urlpatterns = [
    path('Events/',views.events),
    path('Volunteers/',views.Volunteers),
    path('orgs/',views.oranizations),

    path('Event/<int:ed>/',views.event_details),
    path('Volunteer/<int:vd>/',views.Volunteer_details),
    path('Org/<int:od>/',views.Org_details)

    
]