from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

from query.models import User
import logging
# Create your views here.

def select_business_summaries(request):
    #
    return JsonResponse()

def select_business(request):
    #
    return JsonResponse()
