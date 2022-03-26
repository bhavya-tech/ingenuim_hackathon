from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analytics/', include('analytics.urls', 'analytics', namespace='analytics'))
    # Dont modify
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path('', include(('analytics.urls','analytics'),namespace='analytics'))
]
