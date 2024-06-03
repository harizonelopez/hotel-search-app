"""
URL configuration for the hotel_project urls.
"""

from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('get_hotel/', views.get_hotel, name='get_hotel'),
    path('add_hotel/', views.add_hotel, name='add_hotel'),
]
