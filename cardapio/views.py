from rest_framework import viewsets
from .models import Prato
from .serializers import PratoSerializer

class PratoViewSet(viewsets.ModelViewSet):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer