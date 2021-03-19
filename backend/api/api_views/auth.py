from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status as status_codes
from api.helper import db_helper
from query.models import User
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework import generics
import requests
import json
import uuid


class FBAuthAPI(generics.CreateAPIView):
    """FB Auth API"""
    permission_classes = []  # don't need auth

    @csrf_exempt
    def post(self, request):
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
                        password=uuid.uuid4().hex,  # TODO : let user set a password
                        facebook_id=userID,
                        name=name,
                        phone_number=None,
                        isBusiness=False,
                        bio=None)
            user.save()

        # Set auth cookie to request & get / generate auth token
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'user': user.to_dict(), 'token': token.key},
                            status=status_codes.HTTP_200_OK)
