
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

#swagger drf-yasg
schema_view = get_schema_view(
  openapi.Info(
    title="Documentación API Usuarios",
    default_version="v1",
    description="Documentación publica de API Usuarios",
    terms_of_service="https://www.google.com/polices/terms/",
    contact=openapi.Contact(email="jflav.nunez@gmail.com"),
    license=openapi.License(name="BSD License")
  ),
  public=True, 
  permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls, name="users"),
    path('users/', include("apps.users.api.routers")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
