from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Item API",
        default_version='v1',
        description="API для управления предметами",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('items.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', lambda request: HttpResponseRedirect('/swagger/')),
]
