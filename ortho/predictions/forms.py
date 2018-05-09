
#from django import forms

from django.forms import ModelForm
from .models import PredictModel


class PredictForm(ModelForm):

	""" 
		Creating form for entering data for predictions 
	"""
	class Meta:
		model = PredictModel
		exclude = ['create_at', 'Discharge']
		fields = '__all__'
	
