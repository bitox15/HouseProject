from django.urls import path
from apps.users.api import views

urlpatterns = [
    path('user/<int:pk>', views.request_with_pk),
    path('user', views.request_without_pk),

]
