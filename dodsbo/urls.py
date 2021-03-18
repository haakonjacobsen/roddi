from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='dodsbo-home'),
    path('info/', views.info, name='dodsbo-info'),
    path('items/', include('users.urls', namespace='items')),
]
