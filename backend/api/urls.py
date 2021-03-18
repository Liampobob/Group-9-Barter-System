from django.urls import path

from api import api

urlpatterns = [
    path('test', api.test, name='test'),
    path('status', api.status, name='status'),
    path('auth', api.auth, name='auth'),
    path('create_business', api.create_business, name='create_business'),
]
