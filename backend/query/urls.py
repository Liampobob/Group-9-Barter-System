from django.urls import path

from query import business_queries, user_queries

urlpatterns = [
    # selectSingleUser: required:username
    path('selectUser', user_queries.select_user),

    # insertSingleUser: required:username,password
    path('insertUser', user_queries.insert_user),

    # updateSingleUser: required:username ; optional:fields to change
    path('updateUser', user_queries.update_user),

    # selectBusinessSummaries: no parameters
    path('selectBusinessSummaries', business_queries.select_business_summaries),

    # selectBusiness: required: business_username
    path('selectBusiness', business_queries.select_business),
]
