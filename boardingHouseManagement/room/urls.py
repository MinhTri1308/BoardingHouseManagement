from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_room, name='list_room'),
    path('<int:id>/', views.get_information_room, name='information_room'),
    path('addroom/', views.add_room, name='add_room'),
    path('<int:id>/editroom/', views.edit_room, name='edit_room'),
    path('<int:id>/deleteroom/', views.delete_room, name='delete_room'),
    path('guest/', views.create_guests, name='list_guests'),
    path('guest/add_guests/', views.add_guests, name='add_guests'),
    path('guest/search_guest', views.search_guest, name='search_guest'),
    path('<int:id>/guests_in_room/', views.guests_in_room, name='guests_in_room'),
    path('guest/<int:id>/', views.information_guest, name='information_guest'),
    path('guest/edit_guest/<int:guest_id>/', views.edit_guest, name='edit_guest'),
    path('guest/delete_guest/<int:guest_id>/', views.delete_guest, name='delete_guest'),
    path('guest/<int:id>/guest_checkout', views.guest_checkout, name='guest_checkout'),
    path('house/', views.create_house, name='list_house'),
    path('house/add_house/', views.add_house, name='add_house'),
    path('house/<str:nameHouse>/', views.get_information_house, name='information_house'),
    path('house/<str:nameHouse>/get_rooms/', views.get_rooms, name='get_rooms'),
    path('house/<str:nameHouse>/edit_house/', views.edit_house, name='edit_house'),
    path('house/<str:nameHouse>/delete_house/', views.delete_house, name='delete_house'),
    path('electricity/', views.create_electricity, name='electricity'),
    path('calculate/', views.calculate, name='calculate'),
    path('personnel/', views.create_personnel, name='list_personnel'),
    path('personnel/add_personnel/', views.add_personnel, name='add_personnel'),
    path('personnel/<str:fullname>/', views.get_information_personnel, name='information_personnel'),
    path('personnel/<str:fullname>/edit_personnel/', views.edit_personnel, name='edit_personnel'),
    path('personnel/<str:fullname>/delete_personnel/', views.delete_personnel, name='delete_personnel'),
    path('area/', views.create_area, name='list_area'),
    path('area/add_area/', views.add_area, name='add_area'),
    path('area/<int:id>/edit_area/', views.edit_area, name='edit_area'),
    path('area/<int:id>/delete_area/', views.delete_area, name='delete_area'),
]
