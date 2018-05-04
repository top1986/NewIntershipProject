
from django.urls import path
from . import views

app_name='evaluation'
urlpatterns = [
    path('', views.index, name='index'),
]
