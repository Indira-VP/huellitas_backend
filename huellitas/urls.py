from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from mascotas.views import MascotaViewSet
from refugios.views import RefugioViewSet


router = DefaultRouter()
router.register(r'mascotas', MascotaViewSet, basename='mascota')
router.register(r'refugios', RefugioViewSet, basename='refugio')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
