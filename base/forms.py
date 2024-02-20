from django import forms
from .models import Events

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['Event_Description', 'Number_of_Volunteer', 'Size_of_Event', 'Event_Name', 'Location', 'poster', 'Created_Org', 'Registration_option', 'Event_Date', 'Event_Status']
        # You can exclude 'Event_ID' and 'poster_url' since they are auto-generated and calculated fields respectively.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If you want to customize any field, you can do it here
        self.fields['Event_Description'].widget.attrs.update({'class': 'form-control'})
        self.fields['Number_of_Volunteer'].widget.attrs.update({'class': 'form-control'})
        # Similarly, update other fields as needed
