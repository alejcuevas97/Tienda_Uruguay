from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('usuarios.urls')),
    path('api/v1/', include('preferencias.urls')),
    path('api/v1/', include('regalos.urls')),
    path('api/v1/', include('carrito.urls')),
    path('api/v1/', include('pagos.urls')),
    
]
