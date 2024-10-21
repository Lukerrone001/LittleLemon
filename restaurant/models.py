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
    no_of_guest = models.IntegerField
    booking_date = models.DateTimeField(default=datetime.date.today)

#class MenuItem(models.Model):
    #pass