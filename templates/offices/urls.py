from django.urls import path
from . import views

urlpatterns = [
    path('create-district-office/', views.create_district_office, name='create_district_office'),
    path('create-branch-location/', views.create_branch_location, name='create_branch_location'),
]