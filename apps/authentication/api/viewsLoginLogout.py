from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from apps.users.api.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import get_user_model
from apps.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

import datetime
import jwt
from django.conf import settings


@api_view(['POST'])

@permission_classes([AllowAny])
@ensure_csrf_cookie
def login(request):

	User = get_user_model()
	username = request.data.get('username')
	password = request.data.get('password')

	# Error si no se reciben los parametros correspondientes
	if (username is None) or (password is None):
		return Response("Se debe especificar un usuario y una contraseña", status=status.HTTP_412_PRECONDITION_FAILED)

	user = User.objects.filter(username=username).first()

	# Error si usuario no existe o contraseña incorrecta o se encuentra inactivo
	if(user is None) or (not user.is_active) or (not user.check_password(password)):
		return Response("Usuario y/o contraseña inválidos", status=status.HTTP_412_PRECONDITION_FAILED)



	
	access_token_payload = {
		'user_id': user.id,
		'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=600),
		'iat': datetime.datetime.utcnow(),
	}
	access_token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS256')


	serializer = UserSerializer(user)
	response = serializer.data
	response['token'] = access_token
	return Response(response, status=status.HTTP_200_OK)




