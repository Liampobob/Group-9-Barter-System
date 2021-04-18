from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from query.models import Listing
import json

categories = { "Job":'J', "Classes":'C', "To Buy":'B', "To Sell":'S', "CBO":'O'};

class CreateListingAPI(generics.CreateAPIView):
    """Create Mock Jobs API Class"""
    permission_classes = [IsAuthenticated]  # require auth

    def post(self, request):
        data = json.loads(request.body)
        title = data.get('title', None)
        category = data.get('category', None)
        description = data.get('description', None)
        owner = data.get('username', None)
        
        s = Listing(title=title,
                    category=categories[category],
                    description=description,
                    owner=owner)
        s.save()
        return JsonResponse({'data': 1}, status=status_codes.HTTP_200_OK)
