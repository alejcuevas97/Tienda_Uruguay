from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import pago_exitoso,pago_fallido,checkout


urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('pago_exitoso/', pago_exitoso, name='pago_exitoso'),
    path('pago_fallido/', pago_fallido, name='pago_fallido'),
    
]
