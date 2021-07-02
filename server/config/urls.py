from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/', include('api.urls')),
    path('board/', include('board.urls')),
    path('chat/', include('chat.urls')),
]
