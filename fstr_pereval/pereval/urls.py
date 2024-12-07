from django.urls import path, include
from rest_framework import routers
from .views import CoordsViewSet, LevelViewSet, ImagesViewSet, PerevalViewSet

router = routers.SimpleRouter()
router.register(r'coords', CoordsViewSet, basename='coords')
router.register(r'level', LevelViewSet, basename='level')
router.register(r'images', ImagesViewSet, basename='images')
router.register(r'pereval', PerevalViewSet, basename='pereval')

urlpatterns = [
    path('', include(router.urls)),
]