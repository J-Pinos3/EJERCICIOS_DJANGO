
from django.urls import path
#from .views import detail
from . import views

app_name = 'conversation'

urlpatterns = [
    #path('item/detail/<int:pk>', detail, name='detail'),
    path('', views.inbox, name='inbox'),
    path('new/<int:item_pk>/', views.new_conversation, name='new'),

]# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)