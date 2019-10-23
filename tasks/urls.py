from rest_framework.routers import DefaultRouter
from .views import TaskViewset

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tasks', TaskViewset)

urlpatterns = []
urlpatterns += router.urls