from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsAdminOrOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse
# Create your views here.
class TaskLC(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    
    filterset_fields = ["owner", "status"] 
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at"] 

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwnerOrReadOnly]
    lookup_field = 'pk'