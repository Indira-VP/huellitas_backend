from rest_framework.viewsets import ModelViewSet

from .models import Refugio
from .serializers import RefugioSerializer


class RefugioViewSet(ModelViewSet):
    queryset = Refugio.objects.all().order_by('id')
    serializer_class = RefugioSerializer
