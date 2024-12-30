from django.urls import path, include
from .views import MedicamentoView
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="API de Medicamentos",
        default_version='v1',
        description="Documentación interactiva de la API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register('medicamentos', MedicamentoView)


urlpatterns = [
    # path('medicamentos/', views.lista_medicamentos, name= 'lista_medicamentos'),

    # path('', views.lista_medicamentos, name= 'lista_medicamentos'),


    # path('medicamentos/<int:id>/', views.detalle_medicamento, name='detalle_medicamento'),


    # path('medicamentos/nuevo/', views.crear_medicamento, name='crear_medicamento'),

    # path('medicamentos/editar/<int:id>/', views.editar_medicamento, name='editar_medicamento'),

    # path('medicamentos/eliminar/<int:id>/', views.eliminar_medicamento, name='eliminar_medicamento'),

    path('', include(router.urls)), #api/v1
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

