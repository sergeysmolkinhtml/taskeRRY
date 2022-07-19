from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .models import Card,Column,Desk
from .serializers import DeskListSerializer,DeskDetailSerializer,UserSerializer,CardSerializer,ColumnSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import status, viewsets , permissions, generics
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
#desk apis
class DeskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Desk.objects.all()
    serializer_class = DeskListSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Desk.objects.all()
    serializer_class = DeskDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)
    #access via session not token

#user apis
class UserViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many = True)
        return Response(serializer.data)

    def retrieve(self,request,pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'user':serializer.data})

    def update(self,request,*args,**kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({'error':'method update now allowed'})

        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response({'error': 'object doesnt exists'})

        serializer = UserSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'user':serializer.data})

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        elif self.action == 'create' or self.action == 'update':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]



class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer


    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


