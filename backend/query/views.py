from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

from query.models import User
import logging
# Create your views here.

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
