from django.test import TestCase
from restaurant.models import MenuItem, booking
from datetime import datetime
from decimal import Decimal

class MenuItemTest(TestCase):
    def test_create_item(self):
        item = MenuItem.objects.create(title="IceCream", price=Decimal('80'), inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
    def test_default_inventory(self):
        item = MenuItem.objects.create(title="Cake", price=Decimal('50'))
        self.assertEqual(item.inventory, 5)

class bookingTest(TestCase):
    def test_create_booking(self):
        booking = booking.objects.create(
            name="John Doe",
            number_of_guests=4,
            booking_date=datetime(2023, 6, 24, 18, 0)
        )
        expected_str = "John Doe for 4 guests on 2023-06-24 18:00:00"
        self.assertEqual(str(booking), expected_str)
    def test_default_number_of_guests(self):
        booking = booking.objects.create(
            name="Jane Doe",
            booking_date=datetime(2023, 6, 24, 19, 0)
        )
        self.assertEqual(booking.number_of_guests, 6)