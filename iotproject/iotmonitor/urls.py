from django.urls import path
from . import views
from django.conf import settings
from django.template.response import TemplateResponse 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('description/<int:pk>/', views.description, name='description'),
    path('new/', views.new_reading, name='new_reading'),
]

#if settings.DEBUG:
#    urlpatterns += patterns('',(r'^', TemplateResponse, {'template': '404.html'}))