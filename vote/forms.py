from django import forms
from .models import Voting

class VotingForm(forms.ModelForm):
	class Meta:
		model = Voting
		fields = ['voice', 'create',]