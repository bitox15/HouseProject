from django.urls import path
from apps.housing.api import views

urlpatterns = [
    path('housing/<int:pk>', views.request_with_pk),
    path('housing', views.request_without_pk),
  
]




  