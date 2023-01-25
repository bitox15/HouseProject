from django.urls import path
from apps.authentication.api import viewsLoginLogout

urlpatterns = [
    #path('login2/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login', viewsLoginLogout.login),
    
]

