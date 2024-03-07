from django.urls import path
from . import views
from .views import create_event

urlpatterns = [
    path('Events/',views.events),
    path('Volunteers/',views.Volunteers),
    path('orgs/',views.oranizations),
    path('poster/media/<str:pk>/file/', views.ImageFile.as_view()),
    path('create/event/', views.CreateEvent.as_view()),
    path('Event/<int:ed>/',views.event_details),
    path('Volunteer/<int:vd>/',views.Volunteer_details),
    path('Org/<int:od>/',views.Org_details),
    path('newevent/', create_event, name='newevent'),
    path("login/",views.LoginView.as_view(),name = "login"),
    path("reg/volunteer/",views.VolunteerRegisterView.as_view(),name = "register"),
    path("reg/Org/",views.OrgRegisterView.as_view(),name = "OrgRegister"),


 
]