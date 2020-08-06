from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('profile/', include('profileapp.urls')),
]
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
