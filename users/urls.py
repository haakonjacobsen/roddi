from django.urls import path
from .views import favorite_item, items
from django.contrib.auth import views as auth_views
from users import views as user_views

app_name = 'items'


urlpatterns = [
    path('', items, name='items-list'),
    path('favorite/', favorite_item, name='favorite-list')
]
