from .models import Buku
from .serializers import BukuSerializer
from rest_framework import viewsets

class BukuViewset(viewsets.ModelViewSet):
  queryset = Buku.objects.all()
  serializer_class = BukuSerializer