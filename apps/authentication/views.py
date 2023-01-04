from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.api.serializers import UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        token = data['access']
        data.pop('refresh', None)
        data.pop('access', None)

        # Customizo respuesta
        serializer = UserSerializer(self.user)
        respuesta = serializer.data
        respuesta['token'] = token

        return respuesta


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
