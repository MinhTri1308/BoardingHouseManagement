from django.urls import path
from . import views
urlpatterns = [
    path('', views.create, name='list_room'),
    path('<int:id>/', views.get_information_room, name='information_room'),
    path('addroom/', views.add_room, name='add_room'),
    path('editroom/', views.edit_room, name='edit_room'),
    
]
