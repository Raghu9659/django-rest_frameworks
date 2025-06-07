
"""
from django.urls import path
from .views import (
    TodoItemListCreateView,
    TodoItemRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('todos/', TodoItemListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoItemRetrieveUpdateDestroyView.as_view(), name='todo-detail'),
]
"""
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet

router = DefaultRouter()
router.register(r'employees', TodoItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]