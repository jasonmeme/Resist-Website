from django import forms
from crispy_forms.helper import FormHelper
from .models import NewCampaign

class NewCampaignForm(forms.ModelForm):
	class Meta:
		model = NewCampaign
		fields = ['title', 'organizer', 'date', 'location', 'description']
		def __init__(self, *args, **kwargs):
			self.fields['description'].widget.attrs.update(size='40')

class AttendingForm(forms.Form):
	helper = FormHelper()
	attending = forms.BooleanField()			