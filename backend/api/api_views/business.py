from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from api.serializers import BusinessSerializer
from query.models import Business
import json


class BusinessAPI(generics.CreateAPIView):
    """Business API Class"""
    permission_classes = [IsAuthenticated]  # require auth

    def post(self, request):
        data = json.loads(request.body)
        serializer = BusinessSerializer(data=data)
        if serializer.is_valid():
            clean_data = serializer.validated_data
            model = Business(user_id=request.user.id, business_name=clean_data['business_name'], working_days=clean_data['working_days'], work_tags=clean_data['work_tags'],
                             description=clean_data['description'], contact=clean_data['contact'], start_time=clean_data['start_time'], end_time=clean_data['end_time'])
            model.save()
            return JsonResponse({'data': model.to_dict()}, status=status_codes.HTTP_200_OK)
        return JsonResponse({'errors': serializer.errors},
                            status=status_codes.HTTP_400_BAD_REQUEST)

    def get(self, request):
        businesses = Business.objects.filter()
        context = {}
        for b in businesses:
            context[b.user_id] = b.to_dict()

        return JsonResponse(context, status=status_codes.HTTP_200_OK)
