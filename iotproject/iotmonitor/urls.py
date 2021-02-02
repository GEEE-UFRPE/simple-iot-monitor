from django.urls import path
from . import views
from django.conf import settings
from django.template.response import TemplateResponse 

urlpatterns = [
    path('', views.thing_list, name='thing_list'),
    path('thing/<int:pk>/', views.thing_detail, name='thing_detail'),
    path('reading', views.new_reading, name='new_reading'),
]

#if settings.DEBUG:
#    urlpatterns += patterns('',(r'^', TemplateResponse, {'template': '404.html'}))