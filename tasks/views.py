from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['description']