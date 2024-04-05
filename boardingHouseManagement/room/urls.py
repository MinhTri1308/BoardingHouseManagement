from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_room, name='list_room'),
    path('<int:id>/', views.get_information_room, name='information_room'),
    path('addroom/', views.add_room, name='add_room'),
    path('<int:id>/editroom/', views.edit_room, name='edit_room'),
    path('<int:id>/deleteroom/', views.delete_room, name='delete_room'),
    path('house/', views.create_house, name='list_house'),
    path('house/add_house/', views.add_house, name='add_house'),
    path('<str:nameHouse>/get_rooms/', views.get_rooms, name='get_rooms'),
    path('<str:nameHouse>/edit_house/', views.edit_house, name='edit_house'),
    path('<str:nameHouse>/delete_house/', views.delete_house, name='delete_house'),
    path('electricity/', views.create_electricity, name='electricity'),
    path('calculate/', views.calculate, name='calculate'),
]
