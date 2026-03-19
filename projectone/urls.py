from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appone/', include('appone.urls')),
    path('appcbv', include('appcbv.urls')),
]
