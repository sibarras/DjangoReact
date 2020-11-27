from django.contrib import admin
from django.urls import path, include  # nuevo

urlpatterns = [  # Importante colocarle el slash si no es el final
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # nuevo
    path('', include('frontend.urls')),
]
