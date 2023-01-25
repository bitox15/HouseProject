from django.urls import path
from apps.city.api import views

urlpatterns = [
    path('city/<int:pk>', views.request_with_pk),
    path('city', views.request_without_pk),
]

 
