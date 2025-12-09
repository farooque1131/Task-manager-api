from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserListSerializer, UserRoleUpdateSerializer
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserListSerializer

class UpdateUserRoleView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserRoleUpdateSerializer
    lookup_field = "pk"