from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Obmen.kz API",
        default_version='v1',
        description="API documentation for Obmen.kz project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@obmen.kz"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/carts/', include('carts.urls')),
    path('api/v1/reviews/', include('reviews.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/user-messages/', include('user_messages.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
