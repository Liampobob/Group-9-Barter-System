from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

from api.models import User
import logging

def test(request):
    return HttpResponse("Hello, world.")

def status(request):
    return JsonResponse({'status_code':'200', 'status':'Probably Working'})

@csrf_exempt
def auth(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST request are allowed'}, status=400)

    data = json.loads(request.body)
    accessToken = data.get('accessToken', None)

    if accessToken == None:
        return JsonResponse({'error': 'Valid Access Token and UserID must be provided'}, status=401)

    response = requests.get('https://graph.facebook.com/me?access_token=' + accessToken)

    if response.status_code != 200:
        return JsonResponse({'error': 'Invalid access token provided'}, status=401)

    userData = json.loads(response.content)
    accessToken = userData.get('name', None)
    userID = userData.get('id', None)

    if userID == None or accessToken == None:
        return JsonResponse({'error': 'Error when retrieving user details from facebook'}, status=500)

    # TODO : set auth cookie here

    return JsonResponse({'status_code':'200', 'status':'Probably Working'})


def test_db(request):
    logger = logging.getLogger('console')
    s = User(username='sastaffo',
             password='testpass',
             name='Sarah Stafford-Langan',
             phone_number='0810008989',
             isBusiness=False,
             bio = "test bio!")
    s.save()
    users = User.objects.filter(isBusiness=False)
    context = {}
    for u in users:
        context[u.username] = u.to_dict()
    logger.info(json.dumps(context, indent=2))
    return JsonResponse(context)
