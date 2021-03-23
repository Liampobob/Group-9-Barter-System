from django.http import JsonResponse
from rest_framework import status as status_codes
from query.models import User
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
import uuid
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import generics


class HealthAPI(generics.CreateAPIView):
    """Health API Class"""
    permission_classes = []  # don't require auth

    def get(self, request):
        return JsonResponse({"data": "Hello, world."}, status=status_codes.HTTP_200_OK)


class AuthHealthAPI(generics.CreateAPIView):
    """Authentificated Health API Class"""
    permission_classes = [IsAuthenticated]  # require auth

    def get(self, request):
        return JsonResponse(
            {'status': 'user is authentificated',
                'username': request.user.username},
            status=status_codes.HTTP_200_OK)
