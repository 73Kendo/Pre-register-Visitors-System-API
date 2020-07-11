  
from django.urls import path, include
from rest_framework import routers
from .views import GuestViewSet

router = routers.DefaultRouter()
router.register(r'guest', GuestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]