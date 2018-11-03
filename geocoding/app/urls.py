from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/location', views.get_location, name='get_location'),
    path('', views.root, name='root')
]