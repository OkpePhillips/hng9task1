from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def myView(request):
    data = {'slackUsername': 'OkpePhillips', 'backend': True , 'age': 30 , 'bio': 'A python backend developer with passion for building useful applications'}
    return JsonResponse(data)