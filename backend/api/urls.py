from django.urls import path

from api.api_views.auth import FBAuthAPI, AuthAPI, RegisterAPI
from api.api_views.health import HealthAPI, AuthHealthAPI
from api.api_views.business import BusinessAPI
from api.api_views.search import SearchAPI, CreateJobsAPI
from api.api_views.workers import WorkerAPI, UserAPI
from api.api_views.business_reviews import ReviewsAPI

urlpatterns = [
    path('auth', AuthAPI.as_view(), name='auth'),
    path('register', RegisterAPI.as_view(), name='register'),
    path('fb_auth', FBAuthAPI.as_view(), name='fb_auth'),
    path('health', HealthAPI.as_view(), name='health'),
    path('auth_health', AuthHealthAPI.as_view(), name='health_api'),
    path('business', BusinessAPI.as_view(), name='business_api'),
    path('search', SearchAPI.as_view(), name='search_api'),
    path('addJobs', CreateJobsAPI.as_view(), name='add_jobs'),
    path('worker', WorkerAPI.as_view(), name='worker_api'),
    path('me', UserAPI.as_view(), name='user_api'),
    path('review', ReviewsAPI.as_view(), name='business-reviews_api')
]
