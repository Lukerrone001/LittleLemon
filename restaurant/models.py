from django.db import models
import datetime

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(default=6)
    booking_date = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.name} for {self.number_of_guests} guests on {self.booking_date}'