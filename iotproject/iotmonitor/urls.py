from django.urls import path
from . import views
from django.conf import settings
from django.template.response import TemplateResponse

urlpatterns = [
]

#if settings.DEBUG:
#    urlpatterns += patterns('',(r'^', TemplateResponse, {'template': '404.html'}))