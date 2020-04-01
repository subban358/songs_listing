from django import forms
from django.core import validators
from .models import Artists, Songs, Ratings

class DateInput(forms.DateInput):
	input_type = 'date'

class SongInput(forms.ModelForm):
	class Meta:

		model = Songs
		fields = '__all__'
		widgets = {
            'artist': forms.CheckboxSelectMultiple,
            'release_date': DateInput()
        }

class ArtistInput(forms.ModelForm):
	class Meta:
		model = Artists
		fields = '__all__'
		widgets = {
            'dob': DateInput()
        }

class RatingInput(forms.ModelForm):
	class Meta:
		model = Ratings
		fields = ['rating', 'song']
