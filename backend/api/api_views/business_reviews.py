from django.http import JsonResponse
from rest_framework import status as status_codes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from api.serializers import ReviewSerializer
from query.models import User, BusinessReviews
import json


class ReviewsAPI(generics.CreateAPIView):
    """Reviews API Class"""
    permission_classes = [IsAuthenticated]  # require auth

    def post(self, request):
        data = json.loads(request.body)
        serializer = ReviewSerializer(data=data)
        if not serializer.is_valid():
            return JsonResponse({'errors': serializer.errors},
                                status=status_codes.HTTP_400_BAD_REQUEST)
        clean_data = serializer.validated_data

        # TODO : re-add this when business system is done
        # business = Business.objects.filter(
        #     id=clean_data['business_id']).first()
        # if not business:
        #     return JsonResponse({'errors': 'Business ID Provided is invalid'},
        #                         status=status_codes.HTTP_403_FORBIDDEN)

        model = BusinessReviews(
            user_id=request.user.id, business_id=clean_data['business_id'], review_text=clean_data['review_text'], stars=clean_data['stars'])
        model.save()
        return JsonResponse({'data': model.to_dict()}, status=status_codes.HTTP_200_OK)

    def get(self, request):
        business_id = request.GET.get('business_id')
        if business_id is None:
            return JsonResponse({'error': 'business_id must be provided'}, status=status_codes.HTTP_500_INTERNAL_SERVER_ERROR)
        reviews = BusinessReviews.objects.filter(business_id=business_id)
        reviews_response = [b.to_dict() for b in reviews]

        return JsonResponse({'reviews': reviews_response, 'business_id': business_id}, status=status_codes.HTTP_200_OK)
