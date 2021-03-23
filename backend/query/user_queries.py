from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

from query.models import User
import logging
# Create your views here.

def select_user(request):
    if request.method != 'GET':
        return JsonResponse({ 'message' : 'only GET requests allowed' }, status=405)

    u_name = request.GET['username']
    try:
        u = User.objects.get(username=u_name)
        return JsonResponse({ 'message' : 'user found', 'user' : u.to_dict() }, status=200)
    except User.DoesNotExist:
        return JsonResponse({ 'message' : 'user not found' }, status=404)


def insert_user(request):
    if request.method != 'POST':
        return JsonResponse({ 'message' : 'only POST requests allowed' }, status=405)
    else:
        u_name = request.data['username']
        u_pass = request.data['password']
        #u = User()
        return JsonResponse({ 'message' : 'user created successfully' }, status=200)
    #
    return JsonResponse(response)

def update_user(request):
    if request.method != 'POST':
        return JsonResponse({ 'message' : 'only POST requests allowed' }, status=405)
    else:
        return JsonResponse({ 'message' : 'user updated successfully', 'user' : u.to_dict }, status=200)

def delete_user(request):
    return
