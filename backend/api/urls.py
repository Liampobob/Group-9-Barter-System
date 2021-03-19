from django.urls import path

from api.api_views.auth import FBAuthAPI
from api.api_views.health import HealthAPI, AuthHealthAPI
from api.api_views.business import BusinessAPI

urlpatterns = [
    path('fb_auth', FBAuthAPI.as_view(), name='fb_auth'),
    path('health', HealthAPI.as_view(), name='health'),
    path('auth_health', AuthHealthAPI.as_view(), name='health_api'),
    path('business', BusinessAPI.as_view(), name='business_api')
]
