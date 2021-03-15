from django.urls import path

from api import views

urlpatterns = [
    path('test/', api.test, name='test'),
    path('status/', api.status, name='status'),
    path('api/auth', api.auth, name='auth'),
    path('api/create_business', api.create_business, name='create_business'),
]
