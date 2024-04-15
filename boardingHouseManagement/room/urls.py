from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_room, name='list_room'),
    path('<int:id>/', views.get_information_room, name='information_room'),
    path('addroom/', views.add_room, name='add_room'),
    path('search_room/', views.search_roomsNumber, name='search_room'),
    path('<int:id>/get_guest/', views.get_guest, name='get_guest'),
    path('<int:id>/room_not_guest/', views.not_find_guest, name='room_not_guest'),
    path('<int:id>/editroom/', views.edit_room, name='edit_room'),
    path('<int:id>/deleteroom/', views.delete_room, name='delete_room'),
    path('house/', views.create_house, name='list_house'),
    path('house/add_house/', views.add_house, name='add_house'),
    path('house/search_house/', views.search_nameHouse, name='search_house'),
    path('house/<int:id>/', views.get_information_house, name='information_house'),
    path('house/<int:id>/get_rooms/', views.get_rooms, name='get_rooms'),
    path('house/<int:id>/edit_house/', views.edit_house, name='edit_house'),
    path('house/<int:id>/delete_house/', views.delete_house, name='delete_house'),
    path('electricity/', views.create_electricity, name='electricity'),
    path('calculate/', views.calculate, name='calculate'),
    path('personnel/', views.create_personnel, name='list_personnel'),
    path('personnel/add_personnel/', views.add_personnel, name='add_personnel'),
    path('personnel/search_personnel/', views.search_personnel, name='search_personnel'),
    path('personnel/<str:id_personnel>/', views.get_information_personnel, name='information_personnel'),
    path('personnel/<str:id_personnel>/edit_personnel/', views.edit_personnel, name='edit_personnel'),
    path('personnel/<str:id_personnel>/delete_personnel/', views.delete_personnel, name='delete_personnel'),
    path('area/', views.create_area, name='list_area'),
    path('area/add_area/', views.add_area, name='add_area'),
    path('area/search_area/', views.search_area, name='search_area'),
    path('area/<int:id>/get_house', views.get_house, name='get_house'),
    path('area/<int:id>/edit_area/', views.edit_area, name='edit_area'),
    path('area/<int:id>/delete_area/', views.delete_area, name='delete_area'),
    path('list_statistical/', views.statistical, name='list_statistical'),
    path('information_statiscal_guest/', views.statistical_guest, name='information_statistical_guest'),
    path('information_statiscal_electricity/', views.statistical_electricity, name='information_statistical_electricity'),]



