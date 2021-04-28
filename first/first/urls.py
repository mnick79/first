from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings


from women.views import PageNotFound, Error_server

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

handler404 = PageNotFound
handler500 = Error_server
