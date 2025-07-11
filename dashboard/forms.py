# dashboard/forms.py
from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'city', 'service_type', 'phone', 'event_date']
