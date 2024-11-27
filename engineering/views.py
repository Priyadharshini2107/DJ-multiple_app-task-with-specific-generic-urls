from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def EEE(request):
    return HttpResponse( '<h1> EEE is the one of the department in engineering </h1> ')

def Civil(request):
    return HttpResponse(' civil department is the most famous group in engineering')
