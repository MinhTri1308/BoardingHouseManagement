from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Room(models.Model):
    roomsNumber = models.CharField(max_length=50)
    acreage = models.CharField(max_length=10)
    quantity = models.IntegerField(null=True)
    price = models.CharField(max_length=12, null=True)
    interior = models.TextField()

    def __str__(self):
        return self.roomsNumber

class Guests(models.Model):
    fullname = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^(09|03)([0-9]{8})$', message="Số điện thoại có 10 số và bắt đầu bằng 09 hoặc 03")
    phone = models.CharField(validators=[phone_regex], max_length=10)