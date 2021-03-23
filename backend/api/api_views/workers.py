from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from query.models import User


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
