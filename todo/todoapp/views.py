
"""
from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemListCreateView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all().order_by('-created_at')
    serializer_class = TodoItemSerializer

class TodoItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    """
from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer