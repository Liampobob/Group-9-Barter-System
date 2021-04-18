from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from query.models import Listing, User
import json

mockdb = [
    {'title': 'Looking for English Tutor',
     'category': 'J',
     'description': 'Lorem ipsum dolor sit amet'},
    {'title': 'Looking for Manual Labor',
     'category': 'J',
     'description': 'Lorem ipsum dolor sit amet'},
    {'title': 'English Classes',
     'category': 'C',
     'description': 'Lorem ipsum dolor sit amet'},
    {'title': 'Arithmetic Tutoring',
     'category': 'C',
     'description': 'Lorem ipsum dolor sit amet'},
    {'title': 'Selling a used blanket',
     'category': 'S',
     'description': 'Lorem ipsum dolor sit amet'},
    {'title': 'Selling old phone',
     'category': 'S',
     'description': 'Lorem ipsum dolor sit amet'},
    {'title': 'Looking to buy a goat',
     'category': 'B',
     'description': 'Lorem ipsum dolor sit amet'},
    {'title': 'Looking to buy a laptop',
     'category': 'B',
     'description': 'Lorem ipsum dolor sit amet '}
]

categories = { "Jobs":'J', "Classes":'C', "To Buy":'B', "To Sell":'S', "CBOs":'O'};

class SearchAPI(generics.CreateAPIView):
    """Search API Class"""
    permission_classes = [IsAuthenticated]  # require auth

    def post(self, request):
        data = json.loads(request.body)
        terms = data.get('terms', None)
        category = data.get('category', None)
        listings = []
        if(category == 'All'):
            listings = list(map(lambda x: x.to_dict(), Listing.objects.filter(category='O', title__icontains=terms)))
            listings.extend(list(map(lambda x: x.to_dict(), Listing.objects.filter(title__icontains=terms).exclude(category='O'))))
        else:
            listings = list(map(lambda x: x.to_dict(), Listing.objects.filter(category=categories[category], title__icontains=terms))) 

        return JsonResponse({'data': listings}, status=status_codes.HTTP_200_OK)

class CreateJobsAPI(generics.CreateAPIView):
    """Create Mock Jobs API Class"""
    permission_classes = []  # require auth

    x = 0

    def get(self, request):
        
        u = User(username=str(self.x),
                password='test',
                name='test',
                phone_number='test',
                latitude='test',
                longitude='test',
                bio='test',
                isBusiness=False)

        u.save()

        for i in mockdb:
            s = Listing(title=i['title'],
             category=i['category'],
             description = i['description'],
             owner=str(self.x))
            s.save()

        self.x = self.x + 1

        return JsonResponse({'data': 1}, status=status_codes.HTTP_200_OK)
