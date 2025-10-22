from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PratoViewSet

router = DefaultRouter()
router.register(r'pratos', PratoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]