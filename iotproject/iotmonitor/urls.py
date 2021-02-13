from django.urls import path
from . import views

urlpatterns = [
    path('', views.thing_list, name='thing_list'),
    path('things/<int:pk>/', views.thing_detail, name='thing_detail'),
    path('sensors/<int:pk>/readings/csv/', views.export_readings_csv, name='export_readings_csv'),
    path('readings', views.new_reading, name='new_reading'),
]