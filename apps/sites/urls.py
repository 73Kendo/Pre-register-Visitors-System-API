from django.urls import path, include
from rest_framework import routers
from .views import SiteViewSet

router = routers.DefaultRouter()
router.register(r'site', SiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]