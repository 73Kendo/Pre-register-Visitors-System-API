from django.urls import path, include
from rest_framework import routers
from .views import VisitViewSet

router = routers.DefaultRouter()
router.register(r'visit', VisitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]