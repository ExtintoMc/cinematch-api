from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .serializer import UsuariosSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def register(request):
    serializer = UsuariosSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password']) 
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)

    return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        user = User.objects.get(email=request.data['email'])
    except ObjectDoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UsuariosSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data}, status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def profile(request):
    return Response("Estas logueado como {}".format(request.user.username), status=status.HTTP_200_OK)
