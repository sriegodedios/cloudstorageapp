from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
               path('', views.upload_file, name='index'),
               #path('song/<int:id>/', views.song),
               #path('hello-webpack/', TemplateView.as_view(template_name='filemanager/reactupload.html')),
               path('go/', views.upload_file2, name='index'),
            ]