from django.shortcuts import render, get_object_or_404, redirect
from .models import Room
from .forms import ValidatorRoom
# Create your views here.
def create(request):
    data = {'Room': Room.objects.all()}
    return render(request, 'rooms/list_room.html', data)

def get_information_room(request, id):
    information_room = get_object_or_404(Room, id=id)
    return render(request, 'rooms/information_room.html', {'information': information_room})

def add_room(request):
    form = ValidatorRoom()
    if request.method == 'POST':
        form = ValidatorRoom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_room')
    return render(request, 'rooms/add_room.html', {'new': form})



def edit_room(request):
    data = {}
    return render(request, 'rooms/edit_room.html')