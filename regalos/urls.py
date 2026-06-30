from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegaloViewSet

router = DefaultRouter()
router.register(r'regalos', RegaloViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
