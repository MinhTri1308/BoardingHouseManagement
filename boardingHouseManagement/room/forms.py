from django import forms
import re
from .models import Room, House, Electricity

class AddRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['house', 'roomsNumber', 'acreage', 'quantity', 'price', 'interior']

    def clean_roomsNumber(self):
        roomsNumber = self.cleaned_data['roomsNumber']
        try:
            Room.objects.get(roomsNumber=roomsNumber)
        except Room.DoesNotExist:
            return roomsNumber
        raise forms.ValidationError('Số phòng này đã có, vui lòng nhập số phòng khác')
    
    def clean_acreage(self):
        acreage = self.cleaned_data['acreage']
        if acreage <= 0:
            raise forms.ValidationError('Diện tích không thể bằng 0')
        return acreage
    
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise forms.ValidationError('Số lượng không được âm')
        return quantity
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Giá phòng không được âm')
        return price

    def save(self):
        Room.objects.create(house=self.cleaned_data['house'],
                            roomsNumber=self.clean_roomsNumber(),
                            acreage=self.clean_acreage(),
                            quantity=self.clean_quantity(),
                            price=self.clean_price(),
                            interior=self.cleaned_data['interior'])
        
class UpdateInformationRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['house', 'roomsNumber', 'acreage', 'quantity', 'price', 'interior']

    def clean_roomsNumber(self):
        roomsNumber = self.cleaned_data['roomsNumber']
        try:
            Room.objects.get(roomsNumber=roomsNumber)
        except Room.DoesNotExist:
            return roomsNumber
        return roomsNumber
    
    def clean_house(self):
        house = self.cleaned_data['house']
        try:
            Room.objects.get(house=house)
        except Room.DoesNotExist:
            # raise forms.ValidationError('Nhà bạn nhập không tồn tại, vui lòng nhập lại')
            return house
        return house
    
    def clean_acreage(self):
        acreage = self.cleaned_data['acreage']
        if acreage <= 0:
            raise forms.ValidationError('Diện tích không thể bằng 0')
        return acreage
    
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0:
            raise forms.ValidationError('Số lượng không được âm')
        return quantity
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Giá phòng không được âm')
        return price
    
    
class DeleteRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['id']

    def deleteRoom(self, id):
        room = Room.objects.get(id=id)
        room.delete()


class AddHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['nameHouse', 'address']
    
    def clean_nameHouse(self):
        nameHouse = self.cleaned_data['nameHouse']
        try:
            House.objects.get(nameHouse=nameHouse)
        except House.DoesNotExist:
            return nameHouse
        raise forms.ValidationError('Tên nhà bạn nhập đã tồn tại, vui lòng chọn tên nhà khác')
    
    # def clean_address(self):
    #     address = self.cleaned_data['address']
    #     if not re.search(r'(\\S.*),\\s(.*),\\s(Phuong\\s.*),\\s(Quan\\s.*),\\s(Thanh pho\\s.*$)'):
    #         raise forms.ValidationError('Địa chỉ bạn nhập không hợp lệ, vui lòng nhập lại')

    def save(self):
        House.objects.create(nameHouse=self.cleaned_data['nameHouse'], address=self.cleaned_data['address'])


class GetRoomOfHouse(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['house', 'roomsNumber', 'acreage', 'quantity', 'price', 'interior']

    def get_room_of_house(self, nameHouse):
        house = House.objects.get(nameHouse=nameHouse)
        room = Room.objects.filter(house=house)
        return {'inf_room': room}

    

class UpdataInformationHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['nameHouse', 'address']

    def clean_nameHouse(self):
        nameHouse = self.cleaned_data['nameHouse']
        try:
            House.objects.get(nameHouse=nameHouse)
        except House.DoesNotExist:
            return nameHouse
        return nameHouse
        
    def clean_address(self):
        address = self.cleaned_data['address']
        try:
            House.objects.get(address=address)
        except House.DoesNotExist:
            return address
        raise forms.ValidationError('Địa chỉ bạn nhập đã có nhà ròi, vui lòng nhập địa chỉ khác')
    
    
class DeleteHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['nameHouse']
    
    def deleteHouse(self, pk):
        house = House.objects.get(nameHouse=pk)
        house.delete()

        
    
# class CalculateHouse(forms.ModelForm):
#     class Meta:
#         model = Electricity
#         fields = ['house', 'roomsNumber', 'old_electricity', 'new_electricity']
    
#     def calculate_room(self):
#         water = 100 #tính theo đầu người
#         wifi_and_trash = 100
#         #electricity = 
#         cleaner = 100
#         total = 0

