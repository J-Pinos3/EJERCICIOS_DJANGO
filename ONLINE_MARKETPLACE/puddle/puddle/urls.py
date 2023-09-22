from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

#en el primer path, '' siginifca que son las rutas del core
# por defecto
urlpatterns = [
    path('',include('core.urls')),
    path('items/',include('item.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
