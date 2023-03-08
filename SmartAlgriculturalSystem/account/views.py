from django.shortcuts import render
from .models import User
from .serializers import UserSerializer,RegisterUserSerializer
from rest_framework import generics
from rest_framework.parsers import FormParser,MultiPartParser
from rest_framework.permissions import AllowAny, IsAdminUser,IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class RegisterationView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    parser_classes = (FormParser,MultiPartParser)
    permission_classes = (AllowAny, )
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({"user":UserSerializer(user).data,
                         "token": token.key,
                         }, status=status.HTTP_201_CREATED )
    



