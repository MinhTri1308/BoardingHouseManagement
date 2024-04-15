from django import forms
import re
from .models import Room, House, Electricity, Personnel, Area, Guests

#Room
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
            Room.objects.filter(roomsNumber=roomsNumber)
        except Room.DoesNotExist:
            return roomsNumber
        return roomsNumber
    
    def clean_house(self):
        house = self.cleaned_data['house']
        try:
            Room.objects.filter(house=house)
        except Room.DoesNotExist:
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

#House
class AddHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['nameHouse', 'address', 'personnel']
    
    def clean_nameHouse(self):
        nameHouse = self.cleaned_data['nameHouse']
        try:
            House.objects.get(nameHouse=nameHouse)
        except House.DoesNotExist:
            return nameHouse
        raise forms.ValidationError('Tên nhà bạn nhập đã tồn tại, vui lòng chọn tên nhà khác')
    
    def clean_address(self):
        address = self.cleaned_data['address']
        if not re.search(r'^([0-9A-Z]+|[0-9A-Z]+\/[0-9]+),\s((\w+\s\w+\s\w+\s\w+)|(\w+\s\w+\s\w+)|(\w+\s\w+)),\s(Phuong\s[0-9]+),\s(Quan\s[0-9]+),\s(Thanh\spho\s(([A-Z][a-z]+\s[A-Z][a-z]+\s[A-Z][a-z]+)|([A-Z][a-z]+\s[A-Z][a-z]+)|([A-Z][a-z]+)))$', address):
            raise forms.ValidationError('Địa chỉ bạn nhập không đúng')
        try:
            House.objects.get(address=address)
        except House.DoesNotExist:
            return address
        raise forms.ValidationError('Địa chỉ bạn nhập đã có nhà ròi, vui lòng nhập địa chỉ khác')


    def save(self):
        House.objects.create(nameHouse=self.clean_nameHouse(), 
                             address=self.cleaned_data['address'], 
                             personnel=self.cleaned_data['personnel'])


class UpdataInformationHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['nameHouse', 'address', 'personnel']

    def clean_nameHouse(self):
        nameHouse = self.cleaned_data['nameHouse']
        try:
            House.objects.filter(nameHouse=nameHouse)
        except House.DoesNotExist:
            return nameHouse
        return nameHouse
        
    def clean_address(self):
        address = self.cleaned_data['address']
        if not re.search(r'^([0-9A-Z]+|[0-9A-Z]+\/[0-9]+),\s((\w+\s\w+\s\w+\s\w+)|(\w+\s\w+\s\w+)|(\w+\s\w+)),\s(Phuong\s[0-9]+),\s(Quan\s(([0-9]+)|([A-Z][a-z]+\s[A-Z][a-z]+))),\s(Thanh\spho\s(([A-Z][a-z]+\s[A-Z][a-z]+\s[A-Z][a-z]+)|([A-Z][a-z]+\s[A-Z][a-z]+)|([A-Z][a-z]+)))$', address):
            raise forms.ValidationError('Địa chỉ bạn nhập không đúng')
        try:
            House.objects.get(address=address)
        except House.DoesNotExist:
            return address
        raise forms.ValidationError('Địa chỉ bạn nhập đã có nhà ròi, vui lòng nhập địa chỉ khác')

    
    def clean_personnel(self):
        personnel = self.cleaned_data['personnel']
        try:
            House.objects.filter(personnel=personnel)
        except House.DoesNotExist:
            return personnel
        return personnel
    
    
class DeleteHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['nameHouse']
    
    def deleteHouse(self, pk):
        house = House.objects.get(nameHouse=pk)
        house.delete()

class GetRoomOfHouse(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['house', 'roomsNumber', 'acreage', 'quantity', 'price', 'interior']

    def get_room_of_house(self, nameHouse):
        house = House.objects.get(nameHouse=nameHouse)
        room = Room.objects.filter(house=house)
        return {'inf_room': room}
        

# Guest
class AddGuestForm(forms.ModelForm):
    class Meta:
        model = Guests
        fields = ['room','fullname', 'phone', 'date']
        
    def clean_fullname(self):
        fullname = self.cleaned_data['fullname']
        if not re.search(r'^[A-Z][a-z]+\s(?:[A-Z][a-z]+\s?){1,3}[A-Z][a-z]+$', fullname):
            raise forms.ValidationError('Tên không có dấu và viết hoa các kí tự đầu')
        return fullname

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.search(r'^(09|03)([0-9]{8})$', phone):
            raise forms.ValidationError('số điện thoại có 10 số và bắt đầu bằng 09 hoặc 03')
        try:
            Guests.objects.get(phone=phone)
        except Guests.DoesNotExist:
            return phone
        raise forms.ValidationError('số điện thoại bạn nhập đã tồn tại')
          
          
    def check_room(self):
        room = self.cleaned_data['room']
        if room:
            num_guests = Guests.objects.filter(room=room).count()
            if num_guests >= room.quantity:
                self.add_error('room', 'Số lượng khách đã đặt phòng đã đạt đến giới hạn tối đa.')
                # Thêm thông báo lỗi trực tiếp vào trường room của form
        return room

               
    def save(self):
        Guests.objects.create(room=self.cleaned_data['room'],
                              fullname=self.clean_fullname(),
                              phone=self.clean_phone(),
                              date=self.cleaned_data['date'])

    # def save(self, commit=True):
    #     guest = super().save(commit=False)
    #     guest.fullname = self.cleaned_data['fullname']
    #     guest.phone = self.cleaned_data['phone']
    #     if commit:
    #         guest.save()
    #     return guest   
        

class UpdateGuestForm(forms.ModelForm):
    class Meta:
        model = Guests
        fields = ['room','fullname', 'phone', 'date']
        
    def clean_fullname(self):
        fullname = self.cleaned_data['fullname']
        if not re.search(r'^[A-Z][a-z]+\s(?:[A-Z][a-z]+\s?){1,3}[A-Z][a-z]+$', fullname):
            raise forms.ValidationError('Tên không có dấu và viết hoa các kí tự đầu')
        return fullname

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.search(r'^(09|03)([0-9]{8})$', phone):
            raise forms.ValidationError('số điện thoại có 10 số và bắt đầu bằng 09 hoặc 03')
        try:
            Guests.objects.get(phone=phone)
        except Guests.DoesNotExist:
            return phone
        raise forms.ValidationError('số điện thoại bạn nhập đã tồn tại')
                    
               
class DeleteGuestForm(forms.ModelForm):
    class Meta:
        model = Guests
        fields = ['id']
        
    def deleteGuest(self, id):
        guest = Guests.objects.get(id=id)
        guest.delete()

class SearchGuest(forms.ModelForm):
    class Meta:
        model = Guests
        fields = ['fullname'] 
     

# class GetGuestInRoom(forms.ModelForm):
#     class Meta:
#         model = Guests
#     pass
        
        
#Personnel
class AddPersonnel(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['id_personnel', 'fullname', 'phone']

    def clean_id(self):
        id_personnel = self.cleaned_data['id_personnel']
        try:
            Personnel.objects.get(id_personnel=id)
        except Personnel.DoesNotExist:
            return id_personnel
        raise forms.ValidationError('Mã nhân viên này đã tồn tại, vui lòng nhập mã khác')

    def clean_fullname(self):
        fullname = self.cleaned_data['fullname']
        if not re.search(r'^[A-Z][a-z]+\s(?:[A-Z][a-z]+\s?){1,3}[A-Z][a-z]+$', fullname):
            raise forms.ValidationError('Tên bạn nhập không hợp lệ')
        try:
            Personnel.objects.get(fullname=fullname)
        except Personnel.DoesNotExist:
            return fullname
        return fullname

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.search(r'^(09|03)([0-9]{8})$', phone):
            raise forms.ValidationError('số điện thoại có 10 số và bắt đầu bằng 09 hoặc 03')
        try:
            Personnel.objects.get(phone=phone)
        except Personnel.DoesNotExist:
            return phone
        raise forms.ValidationError('số điện thoại bạn nhập đã tồn tại')
        
    def save(self):
        Personnel.objects.create(id_personnel=self.clean_id(), 
                                 fullname=self.clean_fullname(), 
                                 phone=self.clean_phone())

class UpdateInformationPersonnel(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['id_personnel', 'fullname', 'phone']

    def clean_id(self):
        id = self.cleaned_data['id_personnel']
        try:
            Personnel.objects.filter(id_personnel=id)
        except Personnel.DoesNotExist:
            return id
        raise forms.ValidationError('Mã nhân viên này đã tồn tại, vui lòng nhập mã khác')

    def clean_fullname(self):
        fullname = self.cleaned_data['fullname']
        if not re.search(r'^[A-Z][a-z]+\s(?:[A-Z][a-z]+\s?){1,3}[A-Z][a-z]+$', fullname):
            raise forms.ValidationError('Tên bạn nhập không hợp lệ')
        try:
            Personnel.objects.get(fullname=fullname)
        except Personnel.DoesNotExist:
            return fullname
        return fullname

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.search(r'^(09|03)([0-9]{8})$', phone):
            raise forms.ValidationError('số điện thoại có 10 số và bắt đầu bằng 09 hoặc 03')
        try:
            Personnel.objects.get(phone=phone)
        except Personnel.DoesNotExist:
            return phone
        raise forms.ValidationError('số điện thoại bạn nhập đã tồn tại')

class DeletePersonnel(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['id_personnel']

    def deletePersonnel(self, id):
        personnel = Personnel.objects.get(id_personnel=id)
        personnel.delete()

#Area
class AddArea(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nameDistrict']
    
    def clean_district(self):
        discrict = self.cleaned_data['nameDistrict']
        try:
            Area.objects.get(nameDistrict=discrict)
        except Area.DoesNotExist:
            return discrict
        raise forms.ValidationError('Khu vực bạn nhập đã có rồi')
    
    def save(self):
        Area.objects.create(nameDistrict=self.cleaned_data['nameDistrict'])
    
class UpdateArea(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nameDistrict']
    
    def clean_district(self):
        discrict = self.cleaned_data['nameDistrict']
        try:
            Area.objects.get(nameDistrict=discrict)
        except Area.DoesNotExist:
            return discrict
        raise forms.ValidationError('Khu vực bạn nhập đã có rồi')
    
class DeleteArea(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['id']
    
    def deleteArea(self, id):
        area = Area.objects.get(id=id)
        area.delete()
