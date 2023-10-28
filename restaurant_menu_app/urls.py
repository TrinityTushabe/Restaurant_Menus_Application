from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('add/', views.add_menu_item, name='add_menu_item'),
    path('edit/<int:pk>/', views.edit_menu_item, name='edit_menu_item'),
    path('remove/<int:pk>/', views.remove_menu_item, name='remove_menu_item'),
]
