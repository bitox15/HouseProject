from django.urls import path
from apps.city.api import views

urlpatterns = [
    path('city/get/<int:pk>', views.get),
    path('city/list', views.list),
    path('city/create', views.create),
    path('city/update/<int:pk>', views.update),
    path('city/destroy/<int:pk>', views.destroy),
]

 
