  
from django.urls import path, include
from rest_framework import routers
from .views import PurposeViewSet

router = routers.DefaultRouter()
router.register(r'purpose', PurposeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]