from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Electricity, House
from .forms import AddRoom, UpdateInformationRoom, DeleteRoomForm, AddHouse
# Create your views here.
def create_room(request):
    data = {'Room': Room.objects.all()}
    return render(request, 'rooms/list_room.html', data)

def get_information_room(request, id):
    information_room = get_object_or_404(Room, id=id)
    return render(request, 'rooms/information_room.html', {'inf_room': information_room})

def add_room(request):
    form = AddRoom()
    if request.method == 'POST':
        form = AddRoom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_room')
    return render(request, 'rooms/add_room.html', {'new_room': form})

def edit_room(request, id):
    room = get_object_or_404(Room, id=id)
    form = UpdateInformationRoom(instance=room)
    if request.method == 'POST':
        form = UpdateInformationRoom(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('list_room')
    return render(request, 'rooms/edit_room.html', {'update': form, 'inf_room': room})

def delete_room(request, id):
    room = get_object_or_404(Room, id=id)
    form = DeleteRoomForm(instance=room)
    if request.method == 'POST':
        form = DeleteRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.delete_existing()
            return redirect('list_room')
    return render(request, 'rooms/delete_room.html', {'delete': form, 'inf_room': room})


def create_electricity(request):
    data = {'Electricity': Electricity.objects.all().order_by('roomsNumber')}
    return render(request, 'rooms/electricity.html', data)

def information(request, id):
    index = get_object_or_404(Electricity, id=id)
    return render(request, 'rooms/information.html', {'inf_electricity': index})

def create_house(request):
    data = {'House': House.objects.all()}
    return render(request, 'rooms/list_house.html', data)

def information_house(request, id):
    house = get_object_or_404(House, id=id)
    return render(request, 'rooms/information_house.html', {'inf_house': house})

def add_house(request):
    form = AddHouse()
    if request.method == 'POST':
        form = AddHouse(request.POST)
        if form.is_valid():
            form.save()
            redirect('list_room')
    return render(request, 'rooms/add_house.html', {'new_house': form})