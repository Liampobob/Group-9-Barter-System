from django.urls import path

from api import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
]
