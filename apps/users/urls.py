from django.urls import path
from apps.users.api import views

urlpatterns = [
    path('user/get/<int:pk>', views.get),
    path('user/list', views.list),
    path('user/create', views.create),
    path('user/update/<int:pk>', views.update),
    path('user/destroy/<int:pk>', views.destroy),

]
