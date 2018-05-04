from django.shortcuts import render

#import json
# import yaml

def home(request):
    return render(request, 'home.html', None)

def evaluation(request):
    return render(request, 'pages/evaluation.html', {'evaluation':ortho.get_evaluation()})

def monitoring(request):
    return render(request, 'pages/monitoring.html', None)


def management(request):
    return render(request, 'pages/management.html', None)

# def success(request):
#     return render(request, 'pages/success.html', {})
