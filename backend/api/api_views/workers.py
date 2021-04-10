from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from query.models import User
import json


class WorkerAPI(generics.CreateAPIView):
    """Business API Class"""
    permission_classes = [IsAuthenticated]  # require auth

    def get(self, request):
        username = request.GET.get('username')
        if not username:
            return JsonResponse({'error': 'username field must be provided'}, status=status_codes.HTTP_400_BAD_REQUEST)
        user = User.objects.get(username=username)
        print(user)
        return JsonResponse({'user': user.to_dict()}, status=status_codes.HTTP_200_OK)


class UserAPI(generics.CreateAPIView):
    """User API Class"""
    permission_classes = [IsAuthenticated]  # require auth

    def get(self, request):
        username = request.user.username
        if not username:
            return JsonResponse({'error': 'username not found'}, status=status_codes.HTTP_400_BAD_REQUEST)
        user = User.objects.get(username=username)
        print(user)
        return JsonResponse({'user': user.to_dict()}, status=status_codes.HTTP_200_OK)

    def patch(self, request):
        data = json.loads(request.body)
        if not data.get('username') or not data.get('name') or not data.get('phone_number'):
            return JsonResponse({'error': 'expected fields: username name phone_number (bio is optional)'}, status=status_codes.HTTP_403_FORBIDDEN)

        user = User.objects.get(id=request.user.id)
        if not user:
            return JsonResponse({'error': 'user not found'}, status=status_codes.HTTP_500_INTERNAL_SERVER_ERROR)

        user.username = data['username']
        user.name = data['name']
        user.phone_number = data['phone_number']
        user.bio = data['bio']

        try:
            user.save(update_fields=['username',
                      'name', 'bio', 'phone_number'])
        except Exception as e:
            return JsonResponse({'error': 'error saving changes', 'details': e}, status=status_codes.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse({'user': user.to_dict()}, status=status_codes.HTTP_200_OK)
