from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def BBA(request):
    return HttpResponse( ' BBA is the one of the department in artsgroup   ')

def BCOM(request):
    return HttpResponse(' BCOM department is one of the department in artsgroup')

