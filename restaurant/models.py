from django.db import models
import datetime

# Create your models here.
class menu(models.Model):
    title = models.CharField(max_length=255, default="")
    price = models.DecimalField(decimal_places = 2, max_digits= 10, default=0)
    inventory = models.IntegerField

class booking(models.Model):
    no_of_guest = models.IntegerField
    booking_date = models.DateTimeField(default=datetime.date.today)