from django.urls import path
from blog.views import index, detail, create
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('', index, name = "home" ),
    path("create/", create, name = "create-page"),
    path("posts/<int:post_id>/", detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)