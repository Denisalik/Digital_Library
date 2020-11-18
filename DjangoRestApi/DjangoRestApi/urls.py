from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    # Include URL patterns from storage app
    url('api/storage/', include('storage.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)