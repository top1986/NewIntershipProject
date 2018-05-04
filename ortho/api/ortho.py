
from sklearn.externals import joblib
import yaml
import pandas as pd
from django.apps import apps
from predictions.models import PredictModel

# import sys

# path = os.getcwd().split('Orhto')+"/ortho/ml"
# sys.path.append(path)

model = joblib.load('ml/spec_files/models/best_model.sav') # Loading the model at the specified file
trans = joblib.load('ml/spec_files/models/transformer.pkl') # Loading the transformation at the specified file
evaluation = joblib.load('ml/spec_files/models/evaluation')

def clean_data(data):
	"""
		Method 
	"""

	values = []

	with open('spec_files/attributes.yaml', 'r') as attrs:
		attributes = yaml.load(attrs)

	for val in data.values():
		if val == None or val =='':
			values.append('NaN')
		elif val == 'Yes':
			values.append(1)
		elif val == 'No':
			values.append(0)
		else:
			values.append(val)

	return {attr:val for (attr, val) in zip(attributes['attributes'], values)}

def predict(form, action):
	try:

		args = {}

		decision_support = 'No decision'
		message = 'Your prediction is not saved'

		data = clean_data(form.cleaned_data)

		df = pd.DataFrame(data=data,index=[0])

		X = trans.transform(df)
		
		y_pred = model.predict(X)[0]

		if y_pred == 1:
			decision_support = 'We assume that the patient can return home' 
		elif y_pred == 0:
			decision_support = 'We recommend the patient to stay for necessary medical follow-ups'
		else:
			decision_support = 'Nothing is predicted' 


		if action == 'Predict and save':
			message = save_prediction(form, y_pred)

		args['decision_support'] = decision_support
		args['message'] = message

		return args
			
	except Exception as e:
		raise e


def save_prediction(form, y_pred):

	try:
		new_form = form.save(commit=False)
		new_form.y_pred = y_pred
		new_form.save()
		return 'Your prediction has been saved'
	except Exception as e:
		raise e

def get_predictions():
	#PredictModel = apps.get_model('predictions', 'PredictModel')

	predictions = list(PredictModel.objects.values())

	predictions = [{key:clean_prediciton(value) for key, value in obj.items()} for obj in predictions ]

	return predictions

def clean_prediciton(value):
	if value == '' or value == None:
		value = 'NaN'


	return value


	


def get_evaluation():
	# with open('ml/spec_files/models/evaluation', 'rb') as fichier:
	# 	depickler = pickle.Unpickler(fichier)
	# 	evaluation = depickler.load()

	return evaluation#['classification_report']





	