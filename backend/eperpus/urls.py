from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from perpustakaan.viewset import BukuViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('buku', BukuViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
