"""Defining url's patterns for trips"""

from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('city/', views.cities, name='cities'),   ### will need to change the model again.
    path('highlights/<int:city_id>/', views.city_highlights, name='city_highlights'),
    path('new_city/', views.new_trip, name='new_trip'),
    path('new_highlight/<int:c_id>/', views.new_highlights, name='new_highlights'),
    path('edit_highlights/<int:highlight_id>/',views.edit_highlights,name='edit_highlights'),
]
