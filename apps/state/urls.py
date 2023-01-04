from django.urls import path
from apps.state.api import views

urlpatterns = [
    path('state/get/<int:pk>', views.get),
    path('state/list', views.list),
    path('state/create', views.create),
    path('state/update/<int:pk>', views.update),
    path('state/destroy/<int:pk>', views.destroy),
]
