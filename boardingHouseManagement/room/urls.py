from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_room, name='list_room'),
    path('<int:id>/', views.get_information_room, name='information_room'),
    path('addroom/', views.add_room, name='add_room'),
    path('<int:id>/editroom/', views.edit_room, name='edit_room'),
    path('<int:id>/deleteroom/', views.delete_room, name='delete_room'),
    path('electricity/', views.create_electricity, name='electricity'),
    path('list_house', views.create_house, name='list_house'),
    path('<int:id>/', views.information_house, name='information_house'),
    path('add_house/', views.add_house, name='add_house'),

]
