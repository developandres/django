from django.contrib import admin
from django.urls import path
from senaback import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name="login"),
    path('funcion', views.index, name="index"),
    # path('agregar_usuario', views.crear_elemento, name="crear_elemento"),
    # path('transacciones', views.listar_transacciones, name="listar_transacciones")
    path('elementos_consumibles/', views.listar_elementos_consumibles, name='elementos_consumibles'),  # Renombrada para evitar conflicto
    path('Lista-Consumible', views.listar_elementos_consumibles, name="Listar_Consumibles"),
    path('index_consumibles/', views.listar_elementos_consumibles, name='index_consumibles'),
    path('crear_elemento_consumible/', views.crear_elemento_consumible, name='crear_elemento_consumible'),
    path('ruta_para_obtener_elemento/<int:elemento_id>/', views.obtener_elemento, name='obtener_elemento'),
]
