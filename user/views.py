from django.contrib.auth import login
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import Profile
from user.serializers import SignupSerializer, LoginSerializer


# Create your views here.
class SignUp(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    permission_classes = permissions.IsAuthenticated

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['templates']
        login(request, user)
        return Response('You Login Successfully')
