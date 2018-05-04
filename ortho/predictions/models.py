from django.db import models
#from django.forms import ModelForm

# Create your models here.


class PredictModel(models.Model):
	DX_CHOICES=[('GHOA_dx1', 'GHOA_dx1'),
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

	BMI = models.FloatField(verbose_name='Type BMI:')
	AGE_AT_ADMIT = models.IntegerField(verbose_name='Type age:')
	Dx1 = models.CharField(max_length=200, verbose_name='Choose Dx1:', choices=DX_CHOICES, default='GHOA_dx1')
	Dx2 = models.CharField(max_length=200, verbose_name='Choose Dx2:', choices=tuple([('','')]+DX_CHOICES), blank=True)
	Dx3 = models.CharField(max_length=200, verbose_name='Choose Dx3:', choices=tuple([('','')]+DX_CHOICES), blank=True)
	PreOpHgb = models.FloatField(verbose_name='Type PreOpHgb:', blank=True, null=True)
	PreOpCr = models.FloatField(verbose_name='Type PreOpCr:', blank=True, null=True)
	PreOpALC = models.FloatField(verbose_name='Type PreOpALC:', blank=True, null=True)
	PreOpGlucose = models.FloatField(verbose_name='Type PreOpGlucose:', blank=True, null=True)
	PreOpNarcotic = models.FloatField(verbose_name='Type PreOpNarcotic:', blank=True, null=True)
	PreOpDMMeds = models.FloatField(verbose_name='Type PreOpDMMeds:', blank=True, null=True)
	PreOpInsulin = models.FloatField(verbose_name='Type PreOpInsulin:', blank=True, null=True)
	PreOpBloodThinner = models.FloatField(verbose_name='Type PreOpBloodThinner:', blank=True, null=True)
	Side  = models.CharField(max_length=3, verbose_name='Choose side:', choices=(('R', 'R'), ('L','L')), default='R')
	Gender = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	Female = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	arrhythmias = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	valvular = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	pulm_circ = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	PVD = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	HTNw_oCx = models.CharField(max_length=5, verbose_name='TNw/oCx', choices=(('No', 'No'), ('Yes','Yes')), default='No')
	HTNw_Cx = models.CharField(max_length=5, verbose_name='HTNw/Cx', choices=(('No', 'No'), ('Yes','Yes')), default='No')
	Paralysis = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	other_neuro = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	chronic_pulm = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	DMw_oCx = models.CharField(max_length=5, verbose_name='DMw/oCx', choices=(('No', 'No'), ('Yes','Yes')), default='No')
	DMw_Cx = models.CharField(max_length=5, verbose_name='DMw/Cx', choices=(('No', 'No'), ('Yes','Yes')), default='No')
	hypothyroid = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	renal_failure = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	liver_failure = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	PUD = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	AIDS = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	L0oma = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	Mets = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	solidCaw_oMets = models.CharField(max_length=5, verbose_name='solidCaw/oMets', choices=(('No', 'No'), ('Yes','Yes')), default='No')
	RA_CVD = models.CharField(max_length=5, verbose_name='RA/CVD', choices=(('No', 'No'), ('Yes','Yes')), default='No')
	coagulopathy = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	obesity = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	weightLoss = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	fluidElectrolyte = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	bloodLossAnemia = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	DeficiencyAnemia = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	EtOH = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	Drugs = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	Psychosis = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')
	Depression = models.CharField(max_length=5, choices=(('No', 'No'), ('Yes','Yes')), default='No')

	create_at = models.DateField(auto_now_add=True)
	y_pred = models.IntegerField()