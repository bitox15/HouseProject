from django.urls import path
from apps.housing.api import views

urlpatterns = [
    path('housing/get/<int:pk>', views.get),
    path('housing/list', views.list),
    path('housing/create', views.create),
    path('housing/update/<int:pk>', views.update),
    path('housing/destroy/<int:pk>', views.destroy),

]




  