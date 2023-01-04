from django.urls import path
from apps.authentication import viewsLogin

urlpatterns = [
    #path('login2/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login', viewsLogin.login),
]