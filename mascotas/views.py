from rest_framework.viewsets import ModelViewSet

from .models import Mascota
from .serializers import MascotaSerializer


class MascotaViewSet(ModelViewSet):
    queryset = Mascota.objects.select_related('refugio').all().order_by('id')
    serializer_class = MascotaSerializer
