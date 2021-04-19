from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from query.models import Listing
from api.serializers import ListingSerializer
import json

categories = { "Job":'J', "Class":'C', "To Buy":'B', "To Sell":'S', "CBO":'O'};

class CreateListingAPI(generics.CreateAPIView):
    """Create Mock Jobs API Class"""
    permission_classes = [IsAuthenticated]  # require auth

    def post(self, request):
        data = json.loads(request.body)
        serializer = ListingSerializer(data=data);
        if not serializer.is_valid():
            return JsonResponse({'errors': serializer.errors},
                                status=status_code.HTTP_400_BAD_REQUEST)
        clean_data = serializer.validated_data

        model = Listing(title=clean_data['title'],
                        category=clean_data['category'],
                        description=clean_data['description'])
        model.save()
        return JsonResponse({'listing': model.to_dict()}, status=status_codes.HTTP_200_OK)
