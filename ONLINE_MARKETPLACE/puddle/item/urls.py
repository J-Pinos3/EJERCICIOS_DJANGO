from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#from .views import detail
from . import views

app_name = 'item'

urlpatterns = [
    #path('item/detail/<int:pk>', detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    

]# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)