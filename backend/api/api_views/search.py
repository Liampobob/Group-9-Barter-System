from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from query.models import Listing
import json

mockdb = [
    {'title': 'Title1',
     'category': 'Jobs',
     'description': 'Description1'},
    {'title': 'Title2',
     'category': 'Jobs',
     'description': 'Description2'},
    {'title': 'Title3',
     'category': 'Classes',
     'description': 'Description3'},
    {'title': 'Title4',
     'category': 'Classes',
     'description': 'Description4'},
    {'title': 'Title5',
     'category': 'To Sell',
     'description': 'Description5'},
    {'title': 'Title6',
     'category': 'To Sell',
     'description': 'Description6'},
    {'title': 'Title7',
     'category': 'To Buy',
     'description': 'Description7'}
]

class SearchAPI(generics.CreateAPIView):
    """Search API Class"""
    permission_classes = [IsAuthenticated]  # require auth

    def post(self, request):
        data = json.loads(request.body)
        terms = data.get('terms', None)
        category = data.get('category', None)
        listings = []
        if(category == 'All'):
            listings = Listing.objects.filter(title__icontains=terms);
        else:
            listings = Listing.objects.filter(category=category, title__icontains=terms);
        return JsonResponse({'data': list(map(lambda x: x.to_dict(), listings))}, status=status_codes.HTTP_200_OK)


class CreateJobsAPI(generics.CreateAPIView):
    """Create Mock Jobs API Class"""
    permission_classes = []  # require auth

    def get(self, request):
        for i in mockdb:
            s = Listing(title=i['title'],
             category=i['category'],
             description = i['description'])
            s.save()
        return JsonResponse({'data': 1}, status=status_codes.HTTP_200_OK)
