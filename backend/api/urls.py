from django.urls import path

from api import views

urlpatterns = [
    path('', views.test_db, name='database test'),
    path('test/', views.test, name='test'),
    path('status/', views.status, name='status'),
    path('auth/', views.auth, name='auth'),
]
