from django.http import Http404, HttpResponse
from django.forms import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Electricity, House, Personnel, Area, Guests
from .forms import *
import datetime
# Create your views here.


#Room
def create_room(request):
    room = Room.objects.all().order_by('id')
    house = House.objects.all().order_by('id')
    form = AddRoom()
    if request.method == 'POST':
        form = AddRoom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_room')
    return render(request, 'rooms/list_room.html', {'Room': room, 'House': house, 'new_room': form})


def edit_room(request, id):
    house = House.objects.all()
    room = get_object_or_404(Room, id=id)
    form = UpdateInformationRoom(instance=room)
    if request.method == 'POST':
        form = UpdateInformationRoom(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('list_room')
    return render(request, 'rooms/edit_room.html', {'update_room': form, 'inf_room': room, 'House': house})

def delete_room(request, id):
    room = get_object_or_404(Room, id=id)
    form = DeleteRoomForm(instance=room)
    if request.method == 'POST':
        form = DeleteRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.deleteRoom(id)
            return redirect('list_room')
    return render(request, 'rooms/delete_room.html', {'delete_room': form ,'inf_room': room})

def search_roomsNumber(request):
    form = SearchRoom()
    if request.method == 'POST':
        form = SearchRoom(request.POST)
        if form.is_valid():
            roomsNumber = form.cleaned_data['roomsNumber']
            room = Room.objects.filter(roomsNumber=roomsNumber)
    return render(request, 'rooms/search_room.html', {'search_room': form, 'search_roomsNumber': room})


#House
def create_house(request):
    house = House.objects.all()
    area = Area.objects.all()
    personnel = Personnel.objects.all()
    form = AddHouse()
    if request.method == 'POST':
        form = AddHouse(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_house')
    return render(request, 'rooms/list_house.html', {'House': house, 'new_house': form, 'Personnel': personnel, 'Area': area})


def get_rooms(request, id):
    house = House.objects.get(id=id)
    room = Room.objects.filter(house=house)
    return render(request, 'rooms/list_room_of_house.html', {'inf_house': house, 'room_of_house': room})


def edit_house(request, id):
    area = Area.objects.all()
    personnel = Personnel.objects.all()
    house = get_object_or_404(House, id=id)
    form = UpdateInformationHouse(instance=house)
    if request.method == 'POST':
        form = UpdateInformationHouse(request.POST, instance=house)
        if form.is_valid():
            form.save()
            return redirect('list_house')
    return render(request, 'rooms/edit_house.html', {'update_house': form, 'inf_house': house, 'Area': area, 'Personnel': personnel})

def delete_house(request, id):
    house = get_object_or_404(House, id=id)
    form = DeleteHouseForm(instance=house)
    if request.method == 'POST':
        form = DeleteHouseForm(request.POST, instance=house)
        if form.is_valid():
            form.deleteHouse(id)
            return redirect('list_house')
    return render(request, 'rooms/delete_house.html', {'delete_house': form, 'inf_house': house})

def search_nameHouse(request):
    form = SearchHouse()
    if request.method == 'POST':
        form = SearchHouse(request.POST)
        if form.is_valid():
            nameHouse = form.cleaned_data['nameHouse']
            house = House.objects.filter(nameHouse__icontains=nameHouse)
    return render(request, 'rooms/search_house.html', {'search_house': form, 'search_nameHouse': house})

#Electricity
def create_electricity(request):
    electricity = Electricity.objects.all().order_by('id')
    form = ElectricityForm()
    if request.method == 'POST':
        form = ElectricityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_electricity')
    return render(request, 'rooms/list_electricity.html', {'new_electricity': form,'Electricity': electricity, 'House': House.objects.all(), 'Room': Room.objects.all()})

def edit_electricity(request, id):
    electricity = get_object_or_404(Electricity, id=id)
    room = Room.objects.all()
    form = UpdateElectricity(instance=electricity)
    if request.method == 'POST':
        form = UpdateElectricity(request.POST, instance=electricity)
        if form.is_valid():
            form.save()
            return redirect('list_electricity')
    return render(request, 'rooms/edit_electricity.html', {'update_electricity': form, 'inf_electricity': electricity, 'Room': room})

def delete_electricity(request, id):
    electricity = get_object_or_404(Electricity, id=id)
    form = DeleteElectricity(instance=electricity)
    if request.method == 'POST':
        form = DeleteElectricity(request.POST, instance=electricity)
        if form.is_valid():
            form.deleteElectricity(id)
            return redirect('list_electricity')
    return render(request, 'rooms/delete_electricity.html', {'delete_electricity': form, 'inf_electricity': electricity})

def calculate_bill(request, room_id):
    # Lấy chỉ số điện của hai tháng gần nhất của phòng đó
    electricity_readings = Electricity.objects.filter(room=room_id).order_by('-date')[:2]
    if len(electricity_readings) < 2:
        return render(request, 'rooms/calculate_bill.html', {'message': 'Không có đủ dữ liệu để tính toán tiền điện cho phòng này.'})
    
    last_reading = electricity_readings[0].index_electricity
    second_last_reading = electricity_readings[1].index_electricity
    electricity = (last_reading - second_last_reading) * 3.5
    
    room = Room.objects.get(pk=room_id)
    water = room.quantity * 100
    wifi = 100
    room_price = room.price * 1000000
    total = electricity + water + wifi + room_price 
    
    return render(request, 'rooms/calculate_bill.html', {'room_bill': room_price, 'electricity_bill': electricity, 'water_bill': water, 'wifi_bill': wifi, 'total_bill': total})

#Guest
def create_guests(request):
    guest = Guests.objects.all().order_by('id')
    room = Room.objects.all()
    form = AddGuestForm()
    if request.method == 'POST':
        form = AddGuestForm(request.POST)
        if form.is_valid():
            try:
                form.check_room()  # Kiểm tra số lượng khách trong phòng
                form.save()
                return redirect('list_guests')
            except ValidationError as e:
                form.add_error(None, e)  # Thêm lỗi vào form để hiển thị trên template
    
    return render(request, 'rooms/list_guests.html', {'Guests': guest, 'Room':room ,'new_guest': form})

def guests_in_room(request, id):
    room = Room.objects.get(id=id)
    guests = Guests.objects.filter(room=room)
    return render(request, 'rooms/guests_in_room.html', {'room': room, 'guests': guests})


def edit_guest(request, guest_id):
    room = Room.objects.all()                 
    guest = get_object_or_404(Guests, id=guest_id)
    form = UpdateGuestForm(instance=guest)
    if request.method == 'POST':
        form = UpdateGuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('list_guests')
    return render(request, 'rooms/edit_guest.html', {'Room':room,'update_guest': form, 'inf_guest': guest})



def delete_guest(request, guest_id):
    guest = get_object_or_404(Guests, id=guest_id) 
    form = DeleteGuestForm(instance=guest)
    if request.method == 'POST':
        form = DeleteGuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.deleteGuest(guest_id)
            return redirect('list_guests') 
    return render(request, 'rooms/delete_guest.html',{'delete_guest': form,'inf_guest': guest})

def guest_checkout(request, room_id): 
    # Lấy danh sách các khách hàng đang ở trong phòng
    guests = Guests.objects.filter(room_id=room_id)

    if request.method == 'POST':
        # Xử lý khi người dùng bấm nút trả phòng của một khách hàng cụ thể
        guest_id = request.POST.get('guest_id')
        try:
            guest = Guests.objects.get(id=guest_id)
            # Cập nhật room_id của khách hàng thành Null 
            guest.room_id = None # đặt là None thì room sẽ ko lấy đc room_id của khách nên sẽ ko hiện lại trên room
            guest.save()
        except Guests.DoesNotExist:
            pass  
        return redirect('guest_checkout', room_id = room_id)
    return render(request, 'rooms/guest_checkout.html', {'guests':guests,'room_id' : room_id,})



# Search Guest
def search_fullname_guest(request):
    form = SearchGuestByFullnameForm()
    # guests = []
    if request.method == 'POST':
        form = SearchGuestByFullnameForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            guests = Guests.objects.filter(fullname__icontains=fullname)
    return render(request, 'rooms/search_guest.html', {'search_form': form, 'search_guests': guests})

            

#Personnel
def create_personnel(request):
    personnel = Personnel.objects.all()
    form = AddPersonnel()
    if request.method == 'POST':
        form = AddPersonnel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_personnel')
    return render(request, 'rooms/list_personnel.html', {'Personnel': personnel, 'new_personnel': form})


def get_house_of_personnel(request, id_personnel):
    personnel = Personnel.objects.get(id_personnel=id_personnel)
    houses = House.objects.filter(personnel=personnel)
    return render(request, 'rooms/list_house_of_personnel.html', {'inf_personnel': personnel, 'house_of_personnel': houses})

def edit_personnel(request, id_personnel):
    personnel = get_object_or_404(Personnel, id_personnel=id_personnel)
    form = UpdateInformationPersonnel(instance=personnel)
    if request.method == 'POST':
        form = UpdateInformationPersonnel(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('list_personnel')
    return render(request, 'rooms/edit_personnel.html', {'update_personnel': form, 'inf_personnel': personnel})

def delete_personnel(request, id_personnel):
    personnel = get_object_or_404(Personnel, id_personnel=id_personnel)
    form = DeletePersonnel(instance=personnel)
    if request.method == 'POST':
        form = DeletePersonnel(request.POST, instance=personnel)
        if form.is_valid():
            form.deletePersonnel(id_personnel)
            return redirect('list_personnel')
    return render(request, 'rooms/delete_personnel.html', {'delete_personnel': form, 'inf_personnel': personnel})

def search_personnel(request):
    form = SearchPersonnel()
    if request.method == 'POST':
        form = SearchPersonnel(request.POST)
        if form.is_valid():
            lower_str = form.cleaned_data['fullname']
            personnel = Personnel.objects.filter(fullname__icontains=lower_str)
    return render(request, 'rooms/search_personnel.html', {'search_personnel': form, 'search_personnels': personnel})
    
       
#Area
def create_area(request):
    area = Area.objects.all().order_by('id')
    form = AddArea()
    if request.method == 'POST':
        form = AddArea(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_area')
    return render(request, 'rooms/list_area.html', {'Area': area, 'add_area': form})

def get_house_of_area(request, id):
    area = Area.objects.get(id=id)
    house = House.objects.filter(area=area)
    return render(request, 'rooms/list_house_of_area.html', {'inf_area': area, 'house_of_area': house})

def edit_area(request, id):
    area = get_object_or_404(Area, id=id)
    form = UpdateArea(instance=area)
    if request.method == 'POST':
        form = UpdateArea(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect('list_area')
    return render(request, 'rooms/edit_area.html', {'update_area': form, 'inf_area': area})

def delete_area(request, id):
    area = get_object_or_404(Area, id=id)
    form = DeleteArea(instance=area)
    if request.method == 'POST':
        form = DeleteArea(request.POST, instance=area)
        if form.is_valid():
            form.deleteArea(id)
            return redirect('list_area')
    return render(request, 'rooms/delete_area.html', {'delete_area': form, 'inf_area': area})

def search_area(request):
    form = SearchArea()
    if request.method == 'POST':
        form = SearchArea(request.POST)
        if form.is_valid():
            nameDistrict = form.cleaned_data['nameDistrict']
            area = Area.objects.filter(nameDistrict__icontains=nameDistrict)
    return render(request, 'rooms/search_area.html', {'search_area': form, 'search_nameDistrict': area})
            # area = Area.objects.filter(nameDistrict=nameDistrict)
            # return render(request, 'rooms/search_area.html', {'search_area': form, 'search_nameDistrict': area})
        


#statistical
def statistical(request):
    return render(request, 'rooms/list_statistical.html')

def statistical_guest(request):
    form = StatisticalGuest()
    if request.method == 'POST':
        form = StatisticalGuest(request.POST)
        if form.is_valid():
            statistical_guest_month = form.cleaned_data['date']
            guest = Guests.objects.filter(date__year=statistical_guest_month.year, date__month=statistical_guest_month.month)
            guest = guest.annotate(month=ExtractMonth('date'), year=ExtractYear('date'))
            return render(request, 'rooms/information_statistical_guest.html', {'guest': guest, 'form': form})
    # return render(request, 'rooms/information_statistical_guest.html', {'guest': guest, 'form': form})

def statistical_electricity(request):
    
    form = StatisticalElectricity()
    if request.method == 'POST':
        form = StatisticalElectricity(request.POST)
        if form.is_valid():
            statistical_electricity_month = form.cleaned_data['date']
            electricity = Electricity.objects.filter(date__year=statistical_electricity_month.year, date__month=statistical_electricity_month.month)
            electricity = electricity.annotate(month=ExtractMonth('date'), year=ExtractYear('date'))
            return render(request, 'rooms/information_statistical_electricity.html', {'electricity': electricity, 'form': form})
    # return render(request, 'rooms/information_statistical_electricity.html', {'electricity': electricity, 'form': form})

def show_invoice(request, id):
    data = get_object_or_404(Guests, id=id)
    return render(request, 'rooms/invoice.html', {'show_table': True,'g': data })
    
def list_bill(request):
    return render(request,'rooms/list_bill.html')


def information_bill(request):
    data = get_object_or_404(Guests)
    return render(request,'rooms/information_bill.html', {'bill': data})
