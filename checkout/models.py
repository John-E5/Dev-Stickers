from django.db import models
from stickers.models import Sticker


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    date = models.DateField()

    def __str__(self):
        return f'{self.id}, {self.date}, {self.full_name}'


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    sticker = models.ForeignKey(Sticker, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.quantity}, {self.sticker.name}, {self.sticker.price}'
