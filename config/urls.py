from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from config.views import index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name="index"),

    # API routes
    path('categories/', include('apps.category.urls')),
    path('products/', include('apps.product.urls')),
    path('contacts/', include('apps.contact.urls')),

    # --- Swagger / OpenAPI ---
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # ✅ schema manbasi
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),  # ✅ Swagger UI
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
