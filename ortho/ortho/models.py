from django.db import models

class OrthoModel(models.Model):

	list_Dx=[('GHOA_dx1', 'GHOA_dx1'),
		('RCTA_dx1', 'RCTA_dx1'),
		('IA_dx1', 'IA_dx1'),
		('RCT_dx1', 'RCT_dx1'),
		('AVN_dx1', 'AVN_dx1'),
		('PHFx_dx1', 'PHFx_dx1'),
		('Other_dx1', 'Other_dx1'),
		('PHFxSequelae_dx1', 'PHFxSequelae_dx1'),
		('PTA_dx1', 'PTA_dx1'),
		('FailedRCR_dx1', 'FailedRCR_dx1'),
		('failedRCR_dx1', 'failedRCR_dx1')]

	BMI = forms.FloatField(label='Type BMI:', widget=forms.NumberInput, required=False)
	AGE_AT_ADMIT = forms.CharField(label='Type age:', widget=forms.NumberInput, required=False)
	Dx1 = forms.ChoiceField(label='Choose Dx1:', choices=list_Dx)
	Dx2 = forms.ChoiceField(label='Choose Dx2:', choices=tuple([('','')]+list_Dx), required=False)
	Dx3 = forms.ChoiceField(label='Choose Dx3:', choices=tuple([('','')]+list_Dx), required=False)
	PreOpHgb = forms.FloatField(label='Type PreOpHgb:', widget=forms.NumberInput, required=False)
	PreOpCr = forms.FloatField(label='Type PreOpCr:', widget=forms.NumberInput, required=False)
	PreOpALC = forms.FloatField(label='Type PreOpALC:', widget=forms.NumberInput, required=False)
	PreOpGlucose = forms.FloatField(label='Type PreOpGlucose:', widget=forms.NumberInput, required=False)
	PreOpNarcotic = forms.FloatField(label='Type PreOpNarcotic:', widget=forms.NumberInput, required=False)
	PreOpDMMeds = forms.FloatField(label='Type PreOpDMMeds:', widget=forms.NumberInput, required=False)
	PreOpInsulin = forms.FloatField(label='Type PreOpInsulin:', widget=forms.NumberInput, required=False)
	PreOpBloodThinner = forms.FloatField(label='Type PreOpBloodThinner:', widget=forms.NumberInput, required=False)
	Side  = forms.ChoiceField(label='Choose side:', choices=(('R', 'R'), ('L','L')))
	Gender = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	Female = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	arrhythmias = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	valvular = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	pulm_circ = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	PVD = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	HTNw_oCx = forms.ChoiceField(label='TNw/oCx', choices=(('No', 'No'), ('Yes','Yes')))
	HTNw_Cx = forms.ChoiceField(label='HTNw/Cx', choices=(('No', 'No'), ('Yes','Yes')))
	Paralysis = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	other_neuro = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	chronic_pulm = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	DMw_oCx = forms.ChoiceField(label='DMw/oCx', choices=(('No', 'No'), ('Yes','Yes')))
	DMw_Cx = forms.ChoiceField(label='DMw/Cx', choices=(('No', 'No'), ('Yes','Yes')))
	hypothyroid = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	renal_failure = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	liver_failure = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	PUD = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	AIDS = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	L0oma = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	Mets = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	solidCaw_oMets = forms.ChoiceField(label='solidCaw/oMets', choices=(('No', 'No'), ('Yes','Yes')))
	RA_CVD = forms.ChoiceField(label='RA/CVD', choices=(('No', 'No'), ('Yes','Yes')))
	coagulopathy = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	obesity = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	weightLoss = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	fluidElectrolyte = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	bloodLossAnemia = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	DeficiencyAnemia = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	EtOH = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	Drugs = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	Psychosis = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))
	Depression = forms.ChoiceField(choices=(('No', 'No'), ('Yes','Yes')))