from django import forms
import re
from .models import Room, House, Electricity, Personnel, Area, Guests
#Room
class AddRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['house', 'roomsNumber', 'acreage', 'quantity', 'price', 'interior']

    
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
        Room.objects.create(
            house=self.cleaned_data['house'],
            roomsNumber=self.cleaned_data['roomsNumber'],
            acreage=self.clean_acreage(),
            quantity=self.clean_quantity(),
            price=self.clean_price(),
            interior=self.cleaned_data['interior']
        )
        
class UpdateInformationRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['house', 'roomsNumber', 'acreage', 'quantity', 'price', 'interior']
    
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

class SearchRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['roomsNumber']

    
# class GetGuestInRoom(forms.ModelForm):
#     class Meta:
#         model = Guests
#         fields = ['fullname', 'phone', 'date']
    
#     def get_guest_in_room(self, id):
#         room = Room.objects.get(id=id)
#         Guests.objects.get

#House
class AddHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['nameHouse', 'address', 'personnel', 'area']
    
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
            raise forms.ValidationError('Địa chỉ viết không dấu và có dạng: số nhà, tên Đường, Phường gì, Quận gì, Thành phố gì')
        try:
            House.objects.get(address=address)
        except House.DoesNotExist:
            return address
        raise forms.ValidationError('Địa chỉ bạn nhập đã có nhà ròi, vui lòng nhập địa chỉ khác')

    def clean_area(self):
        area = self.cleaned_data['area']
        address = self.cleaned_data['address']
        find_area = re.search(r'(Quan\s[0-9]+)', address)

        if area != find_area:
            raise forms.ValidationError('Khu vực bạn chọn không khớp với địa chỉ nhà, vui lòng chọn lại')
        return area

    def save(self):
        House.objects.create(nameHouse=self.clean_nameHouse(), 
                             address=self.clean_address(), 
                             personnel=self.cleaned_data['personnel'],
                             area=self.cleaned_data['area'])


class UpdataInformationHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['nameHouse', 'address', 'personnel', 'area']

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
            raise forms.ValidationError('Địa chỉ viết không dấu và có dạng: số nhà, tên Đường, Phường gì, Quận gì, Thành phố gì')
        try:
            House.objects.get(address=address)
        except House.DoesNotExist:
            return address
        raise forms.ValidationError('Địa chỉ bạn nhập đã có nhà ròi, vui lòng nhập địa chỉ khác')

    
    
class DeleteHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['id']
    
    def deleteHouse(self, id):
        house = House.objects.get(id=id)
        house.delete()
       
class SearchHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['nameHouse']

#Personnel
class AddPersonnel(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['id_personnel', 'fullname', 'phone']

    def clean_id(self):
        id_personnel = self.cleaned_data['id_personnel']
        if not re.search(r'^(NV)[0-9]+$', id_personnel):
            raise forms.ValidationError('Mã nhân viên có dạng NV"số". VD: NV1, NV42, ...')
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
        Personnel.objects.create(id_personnel=self.clean_id(), fullname=self.clean_fullname(), phone=self.clean_phone())

class UpdateInformationPersonnel(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['id_personnel', 'fullname', 'phone']

    def clean_id(self):
        id_personnel = self.cleaned_data['id_personnel']
        if not re.search(r'^(NV)[0-9]+$', id_personnel):
            raise forms.ValidationError('Mã nhân viên có dạng NV"số". VD: NV1, NV42, ...')
        try:
            Personnel.objects.filter(id_personnel=id_personnel)
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

class DeletePersonnel(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['id_personnel']

    def deletePersonnel(self, id):
        personnel = Personnel.objects.get(id_personnel=id)
        personnel.delete()

class SearchPersonnel(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['id_personnel']

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

class SearchArea(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nameDistrict']