from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import CustomerViewSet, OrderViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Initialize a global router for other app-specific views
router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'orders', OrderViewSet, basename='order')

schema_view = get_schema_view(
    openapi.Info(
        title="Software engineering lab",
        default_version="v1",
        description="API documentation for the lab",
        ),
    public=True,
    permission_classes=(AllowAny,),
    authentication_classes=[],
)

# Define global URL patterns
urlpatterns = [
    path('api/', include(router.urls)),  # Includes customer and order routes
    path('api/', include('myapp.urls')),  # Includes product routes and JWT token endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
