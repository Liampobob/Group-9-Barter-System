from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from api.serializers import WorkerSerializer
import requests
import json
from rest_framework import status as status_codes


def test(request):
    return HttpResponse("Hello, world.")


def status(request):
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
    accessToken = userData.get('name', None)
    userID = userData.get('id', None)

    if userID == None or accessToken == None:
        return JsonResponse(
            {'error': 'Error when retrieving user details from facebook'},
            status=status_codes.HTTP_500_INTERNAL_SERVER_ERROR)

    # TODO : set auth cookie here

    return JsonResponse({'status': 'work in progress'},
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
