from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from api.serializers import WorkerSerializer
import requests
import json
from rest_framework import status as status_codes
import api.db_helper as db_helper
from query.models import User
from django.contrib.auth import login

def test(request):
    return HttpResponse("Hello, world.")


def status(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status': 'NOPE'},
                        status=status_codes.HTTP_200_OK)
    return JsonResponse({'status': 'Probably Working'},
                        status=status_codes.HTTP_200_OK)


@csrf_exempt
@require_http_methods(["POST"])
def auth(request):
    data = json.loads(request.body)
    accessToken = data.get('accessToken', None)

    if accessToken == None:
        return JsonResponse(
            {'error': 'Valid Access Token and UserID must be provided'},
            status=status_codes.HTTP_401_UNAUTHORIZED)

    response = requests.get('https://graph.facebook.com/me?access_token=' +
                            accessToken)

    if response.status_code != 200:
        return JsonResponse({'error': 'Invalid access token provided'},
                            status=status_codes.HTTP_401_UNAUTHORIZED)

    userData = json.loads(response.content)
    name = userData.get('name', None)
    userID = userData.get('id', None)

    if userID == None or name == None:
        return JsonResponse(
            {'error': 'Error when retrieving user details from facebook'},
            status=status_codes.HTTP_500_INTERNAL_SERVER_ERROR)

    user = db_helper.get_user_by_fb_id(userID)
    # Register user automatically if does not exist already
    if user == None:
        # register user
        user = User(username=userID,  # TODO : let user set a username
                 password=None,
                 name=name,
                 phone_number=None,
                 isBusiness=False,
                 bio=None)
        user.save()

    # Set auth cookie to request
    login(request, user)
    return JsonResponse({'user': user.to_dict()},
                        status=status_codes.HTTP_200_OK)


@csrf_exempt
@require_http_methods(["POST"])
def create_business(request):
    data = json.loads(request.body)
    serializer = WorkerSerializer(data=data)
    if serializer.is_valid():
        model = serializer.validated_data
        # TODO : store locally
        return JsonResponse({'data': model}, status=status_codes.HTTP_200_OK)
    return JsonResponse({'errors': serializer.errors},
                        status=status_codes.HTTP_400_BAD_REQUEST)
