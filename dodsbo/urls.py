from django.urls import path
from .views import EstateListView, EstateDetailView
from . import views

urlpatterns = [
    path('', views.home, name='dodsbo-home'),
    path('estate/<int:pk>/', EstateDetailView.as_view(), name='estate-detail'),
    path('estates/', EstateListView.as_view(), name='dodsbo-info'),
]
