from django.urls import path
from apps.state.api import views

urlpatterns = [
    path('state/<int:pk>', views.request_with_pk),
    path('state', views.request_without_pk),
]
