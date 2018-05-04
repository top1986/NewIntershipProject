from django.shortcuts import render
from .forms import PredictForm
from api import ortho

# Create your views here.


def index(request):

	# with open('spec_files/attributes.yaml', 'r') as attrs:
	#     attributes = yaml.load(attrs)



	if request.method == 'POST':
		form = PredictForm(request.POST)

		if form.is_valid():
			args = ortho.predict(form, request.POST.get('predict'))

			return render(request, 'pages/success.html', {'args': args})
	else:
		form = PredictForm() 
	return render(request, 'predictions/index.html', {'form':form})

def show(request):
	return render(request, 'predictions/show_predictions.html', {'predictions': ortho.get_predictions()})


# def show(request):
# 	predictions = PredictModel.objects.all()
# 	return render(request, 'predictions/show_predictions.html', {'predictions': predictions})