from django.urls import path, include
from rest_framework import routers
from .views import DeviceViewset, CategoryViewset, TaskViewset

router = routers.DefaultRouter()
router.register(r'device', DeviceViewset)
router.register(r'category', CategoryViewset)
router.register(r'task', TaskViewset)

urlpatterns = [
    path('', include(router.urls))
]
