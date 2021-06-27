from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('database/', include('database.urls')),
    path('', include('app.urls')),
]
