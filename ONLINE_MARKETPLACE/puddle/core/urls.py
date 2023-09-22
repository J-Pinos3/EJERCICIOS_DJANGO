from django.urls import path
from . import views

app_name = 'core'

#remuevo el url que esta en  puddle.urls.py
#path('contact/', contact, name='contact'),
urlpatterns = [

    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('signup/',views.signup, name='signup'),

]