from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from query.models import Listing
import json

mockdb = [
    {'title': 'Looking for English Tutor',
     'category': 'Jobs',
     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam at pulvinar nisl, in lacinia metus. Aenean non pulvinar dui. Vestibulum viverra at lectus sit amet aliquet. Ut luctus fringilla lacus, sit amet tempor mauris. Nulla cursus magna vel ipsum vestibulum, at gravida purus condimentum. In lobortis, quam eu dignissim ornare, elit odio rutrum lacus, sit amet gravida augue libero id est. Fusce dictum dui sed est vulputate, ac facilisis est varius. Pellentesque viverra purus id nisl dictum, id blandit nunc ornare. Ut vehicula tempor ipsum, iaculis aliquam nulla auctor nec. Morbi tincidunt ipsum in nisi pretium tempus. Proin eleifend eleifend urna, eu vehicula justo. Suspendisse aliquet fringilla tortor. Sed tempor, augue sit amet porta imperdiet, metus dui dapibus augue, id interdum felis velit quis elit. Integer ligula diam, accumsan pellentesque lacus at, tristique sodales turpis. Nulla condimentum vitae mauris at bibendum. Etiam sed odio volutpat, efficitur libero ut, ultricies magna. '},
    {'title': 'Looking for Manual Labor',
     'category': 'Jobs',
     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam at pulvinar nisl, in lacinia metus. Aenean non pulvinar dui. Vestibulum viverra at lectus sit amet aliquet. Ut luctus fringilla lacus, sit amet tempor mauris. Nulla cursus magna vel ipsum vestibulum, at gravida purus condimentum. In lobortis, quam eu dignissim ornare, elit odio rutrum lacus, sit amet gravida augue libero id est. Fusce dictum dui sed est vulputate, ac facilisis est varius. Pellentesque viverra purus id nisl dictum, id blandit nunc ornare. Ut vehicula tempor ipsum, iaculis aliquam nulla auctor nec. Morbi tincidunt ipsum in nisi pretium tempus. Proin eleifend eleifend urna, eu vehicula justo. Suspendisse aliquet fringilla tortor. Sed tempor, augue sit amet porta imperdiet, metus dui dapibus augue, id interdum felis velit quis elit. Integer ligula diam, accumsan pellentesque lacus at, tristique sodales turpis. Nulla condimentum vitae mauris at bibendum. Etiam sed odio volutpat, efficitur libero ut, ultricies magna. '},
    {'title': 'English Classes',
     'category': 'Classes',
     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam at pulvinar nisl, in lacinia metus. Aenean non pulvinar dui. Vestibulum viverra at lectus sit amet aliquet. Ut luctus fringilla lacus, sit amet tempor mauris. Nulla cursus magna vel ipsum vestibulum, at gravida purus condimentum. In lobortis, quam eu dignissim ornare, elit odio rutrum lacus, sit amet gravida augue libero id est. Fusce dictum dui sed est vulputate, ac facilisis est varius. Pellentesque viverra purus id nisl dictum, id blandit nunc ornare. Ut vehicula tempor ipsum, iaculis aliquam nulla auctor nec. Morbi tincidunt ipsum in nisi pretium tempus. Proin eleifend eleifend urna, eu vehicula justo. Suspendisse aliquet fringilla tortor. Sed tempor, augue sit amet porta imperdiet, metus dui dapibus augue, id interdum felis velit quis elit. Integer ligula diam, accumsan pellentesque lacus at, tristique sodales turpis. Nulla condimentum vitae mauris at bibendum. Etiam sed odio volutpat, efficitur libero ut, ultricies magna. '},
    {'title': 'Arithmetic Tutoring',
     'category': 'Classes',
     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam at pulvinar nisl, in lacinia metus. Aenean non pulvinar dui. Vestibulum viverra at lectus sit amet aliquet. Ut luctus fringilla lacus, sit amet tempor mauris. Nulla cursus magna vel ipsum vestibulum, at gravida purus condimentum. In lobortis, quam eu dignissim ornare, elit odio rutrum lacus, sit amet gravida augue libero id est. Fusce dictum dui sed est vulputate, ac facilisis est varius. Pellentesque viverra purus id nisl dictum, id blandit nunc ornare. Ut vehicula tempor ipsum, iaculis aliquam nulla auctor nec. Morbi tincidunt ipsum in nisi pretium tempus. Proin eleifend eleifend urna, eu vehicula justo. Suspendisse aliquet fringilla tortor. Sed tempor, augue sit amet porta imperdiet, metus dui dapibus augue, id interdum felis velit quis elit. Integer ligula diam, accumsan pellentesque lacus at, tristique sodales turpis. Nulla condimentum vitae mauris at bibendum. Etiam sed odio volutpat, efficitur libero ut, ultricies magna. '},
    {'title': 'Selling a used blanket',
     'category': 'To Sell',
     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam at pulvinar nisl, in lacinia metus. Aenean non pulvinar dui. Vestibulum viverra at lectus sit amet aliquet. Ut luctus fringilla lacus, sit amet tempor mauris. Nulla cursus magna vel ipsum vestibulum, at gravida purus condimentum. In lobortis, quam eu dignissim ornare, elit odio rutrum lacus, sit amet gravida augue libero id est. Fusce dictum dui sed est vulputate, ac facilisis est varius. Pellentesque viverra purus id nisl dictum, id blandit nunc ornare. Ut vehicula tempor ipsum, iaculis aliquam nulla auctor nec. Morbi tincidunt ipsum in nisi pretium tempus. Proin eleifend eleifend urna, eu vehicula justo. Suspendisse aliquet fringilla tortor. Sed tempor, augue sit amet porta imperdiet, metus dui dapibus augue, id interdum felis velit quis elit. Integer ligula diam, accumsan pellentesque lacus at, tristique sodales turpis. Nulla condimentum vitae mauris at bibendum. Etiam sed odio volutpat, efficitur libero ut, ultricies magna. '},
    {'title': 'Selling old phone',
     'category': 'To Sell',
     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam at pulvinar nisl, in lacinia metus. Aenean non pulvinar dui. Vestibulum viverra at lectus sit amet aliquet. Ut luctus fringilla lacus, sit amet tempor mauris. Nulla cursus magna vel ipsum vestibulum, at gravida purus condimentum. In lobortis, quam eu dignissim ornare, elit odio rutrum lacus, sit amet gravida augue libero id est. Fusce dictum dui sed est vulputate, ac facilisis est varius. Pellentesque viverra purus id nisl dictum, id blandit nunc ornare. Ut vehicula tempor ipsum, iaculis aliquam nulla auctor nec. Morbi tincidunt ipsum in nisi pretium tempus. Proin eleifend eleifend urna, eu vehicula justo. Suspendisse aliquet fringilla tortor. Sed tempor, augue sit amet porta imperdiet, metus dui dapibus augue, id interdum felis velit quis elit. Integer ligula diam, accumsan pellentesque lacus at, tristique sodales turpis. Nulla condimentum vitae mauris at bibendum. Etiam sed odio volutpat, efficitur libero ut, ultricies magna. '},
    {'title': 'Looking to buy a goat',
     'category': 'To Buy',
     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam at pulvinar nisl, in lacinia metus. Aenean non pulvinar dui. Vestibulum viverra at lectus sit amet aliquet. Ut luctus fringilla lacus, sit amet tempor mauris. Nulla cursus magna vel ipsum vestibulum, at gravida purus condimentum. In lobortis, quam eu dignissim ornare, elit odio rutrum lacus, sit amet gravida augue libero id est. Fusce dictum dui sed est vulputate, ac facilisis est varius. Pellentesque viverra purus id nisl dictum, id blandit nunc ornare. Ut vehicula tempor ipsum, iaculis aliquam nulla auctor nec. Morbi tincidunt ipsum in nisi pretium tempus. Proin eleifend eleifend urna, eu vehicula justo. Suspendisse aliquet fringilla tortor. Sed tempor, augue sit amet porta imperdiet, metus dui dapibus augue, id interdum felis velit quis elit. Integer ligula diam, accumsan pellentesque lacus at, tristique sodales turpis. Nulla condimentum vitae mauris at bibendum. Etiam sed odio volutpat, efficitur libero ut, ultricies magna. '},
    {'title': 'Looking to buy a laptop',
     'category': 'To Buy',
     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam at pulvinar nisl, in lacinia metus. Aenean non pulvinar dui. Vestibulum viverra at lectus sit amet aliquet. Ut luctus fringilla lacus, sit amet tempor mauris. Nulla cursus magna vel ipsum vestibulum, at gravida purus condimentum. In lobortis, quam eu dignissim ornare, elit odio rutrum lacus, sit amet gravida augue libero id est. Fusce dictum dui sed est vulputate, ac facilisis est varius. Pellentesque viverra purus id nisl dictum, id blandit nunc ornare. Ut vehicula tempor ipsum, iaculis aliquam nulla auctor nec. Morbi tincidunt ipsum in nisi pretium tempus. Proin eleifend eleifend urna, eu vehicula justo. Suspendisse aliquet fringilla tortor. Sed tempor, augue sit amet porta imperdiet, metus dui dapibus augue, id interdum felis velit quis elit. Integer ligula diam, accumsan pellentesque lacus at, tristique sodales turpis. Nulla condimentum vitae mauris at bibendum. Etiam sed odio volutpat, efficitur libero ut, ultricies magna. '}
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
