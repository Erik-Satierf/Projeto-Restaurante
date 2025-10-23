from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteviewSet

router = DefaultRouter()
router.register(r'clientes', ClienteviewSet)

urlpatterns = [
    path('', include(router.urls)),
]