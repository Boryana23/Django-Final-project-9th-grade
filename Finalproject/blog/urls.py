from django.urls import path
from blog.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name = "home" ),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)