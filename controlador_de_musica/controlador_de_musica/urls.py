from django.contrib import admin
from django.urls import path, include  # nuevo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # nuevo
    path('', include('frontend.urls'))
]
