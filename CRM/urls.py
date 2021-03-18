from django.urls import path
from .views import lista_clientes, detalle_cliente, nuevo_cliente, busca_cliente, editar_cliente, lista_comerciales, descargarcsv, detalle_comercial, descargarcom

app_name = "CRM"

urlpatterns = [
    path('clientes/', lista_clientes),
    path('clientes/nuevo/', nuevo_cliente),
    path('clientes/buscador/', busca_cliente),
    path('clientes/comerciales/', lista_comerciales),
    path('clientes/buscador/descargar', descargarcsv),#???????????????
    path('clientes/<pk>/', detalle_cliente),
    path('editar/<pk>/', editar_cliente),
    path('comerciales/<pk>', detalle_comercial),
    path('clientes/comerciales/descargar', descargarcom),
]