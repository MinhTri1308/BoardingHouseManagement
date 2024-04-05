from django.db import models

# Create your models here.
class House(models.Model):
    nameHouse = models.CharField(primary_key=True, max_length=100, null=False)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nameHouse

class Room(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True)
    roomsNumber = models.IntegerField()
    acreage = models.IntegerField()
    quantity = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    interior = models.TextField()


class Guests(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

class Electricity(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True)
    roomsNumber = models.ForeignKey(Room, on_delete=models.CASCADE)
    old_electricity = models.IntegerField()
    new_electricity = models.IntegerField()

    def calulate_electricity(self):
        return self.new_electricity - self.old_electricity
    
    #override method save() in models.Model is django
    def save(self, *args, **kwargs):
        self.use_electricity = self.calulate_electricity()
        super(Electricity, self).save(*args, **kwargs)

class Calculatator(models.Model):
    use_electricity = models.ForeignKey(Electricity, on_delete=models.CASCADE)
    water = models.IntegerField(default=100)
    wifi_and_trash = models.IntegerField(default=100)
    cleaner = models.IntegerField(default=100)
    
