from django.shortcuts import render, get_object_or_404
from .models import Room
from django.http import Http404
# Create your views here.
def create(request):
    data = {'Room': Room.objects.all()}
    return render(request, 'rooms/list_room.html', data)

def get_information_room(request, id):
    information_room = Room.objects.get(id=id)
    # try:
    #     get_room = Room.objects.get(id=id)
    # except Room.DoesNotExist:
    #     raise Http404('Phòng không tồn tại')
    return render(request, 'rooms/information_room.html', {'information': information_room})