from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dodsbo-home'),
    path('info/', views.info, name='dodsbo-info'),
]
