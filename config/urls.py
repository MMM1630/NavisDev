from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include("navis.urls")),
    path('api/ckeditor/', include('ckeditor_uploader.urls')),  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
