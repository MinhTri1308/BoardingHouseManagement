from django.urls import path
from . import views
urlpatterns = [
    path('', views.create, name='list_room'),
    path('<int:id>/', views.get_information_room, name='information_room'),
]
