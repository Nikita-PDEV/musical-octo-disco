from django.urls import path, include
from rest_framework import routers
from .views import PassUserViewSet

router = routers.SimpleRouter()
router.register(r'users', PassUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]