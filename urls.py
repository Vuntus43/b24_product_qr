from django.contrib import admin
from django.urls import path, include
from django.conf import settings                # ← добавь
from django.conf.urls.static import static      # ← добавь

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products_qr.urls')),
]

if settings.DEBUG:                               # ← добавь
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
