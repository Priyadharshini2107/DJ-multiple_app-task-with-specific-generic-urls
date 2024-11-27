from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def cs(request):
    return HttpResponse( '<h1> computerscience is the one of the department in sciencegroup  </h1> ')

def maths(request):
    return HttpResponse(' maths department is one of the department in sciencegroup')
