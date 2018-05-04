from django.shortcuts import render

from api import ortho

# Create your views here.

def index(request):
	return render(request, 'evaluation/index.html', {'evaluation':ortho.get_evaluation()})
