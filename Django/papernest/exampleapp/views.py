import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse('Index Page')

def papernest(request):
    return render(request, 'exampleapp/papernest.html', {})
