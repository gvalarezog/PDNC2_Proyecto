"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from personas.views import agregar_persona, ver_persona, eliminar_persona, modificar_persona, generar_reporte, \
    PersonaViewSet, CursoViewSet
from webapp.views import bienvenida, despedida, mostrar_edad, bienvenida2

router = routers.DefaultRouter()
router.register(r'api_personas', PersonaViewSet)
router.register(r'api_cursos', CursoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',bienvenida2, name='inicio'),
    path('agregar_persona/',agregar_persona),
    path('ver_persona/<int:id>',ver_persona),
    path('eliminar_persona/<int:id>',eliminar_persona),
    path('modificar_persona/<int:id>',modificar_persona),
    path('generar_reporte/',generar_reporte),
]
urlpatterns += router.urls
