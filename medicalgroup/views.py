from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def cardilogy(request):
    return HttpResponse( '<h1>cardilogy:</h1>Is the special group in medical department for human heart defects,heart failure ')

def neurology(request):
    return HttpResponse(' <h1>Neurology:</h1> Is the special group in medical department for deals with human nervous system')
