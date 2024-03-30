from django.db import models

# Create your models here.
class House(models.Model):
    nameHouse = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)

class Room(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True)
    roomsNumber = models.IntegerField()
    acreage = models.IntegerField()
    quantity = models.IntegerField(null=True)
    price = models.CharField(max_length=12, null=True)
    interior = models.TextField()


class Guests(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

class Electricity(models.Model):
    roomsNumber = models.ForeignKey(Room, on_delete=models.CASCADE)
    old_electricity = models.IntegerField()
    new_electricity = models.IntegerField()

    def calulate_electricity(self):
        return self.new_electricity - self.old_electricity
    
    #override method save() in models.Model is django
    def save(self, *args, **kwargs):
        self.use_electricity = self.calulate_electricity()
        super(Electricity, self).save(*args, **kwargs)

