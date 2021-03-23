from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from api.serializers import WorkerSerializer
import json


class BusinessAPI(generics.CreateAPIView):
    """Business API Class"""
    permission_classes = [IsAuthenticated]  # require auth

    def post(self, request):
        data = json.loads(request.body)
        serializer = WorkerSerializer(data=data)
        if serializer.is_valid():
            model = serializer.validated_data
            # TODO : store locally
            return JsonResponse({'data': model}, status=status_codes.HTTP_200_OK)
        return JsonResponse({'errors': serializer.errors},
                            status=status_codes.HTTP_400_BAD_REQUEST)
