from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=200,verbose_name='Nazwa firmy')
    description = models.CharField(max_length=1000, verbose_name='Opis firmy')
    email = models.EmailField(verbose_name='Email')
    password = models.CharField(max_length=40, verbose_name='Hasło')


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    address_type = models.CharField(max_length=40, choices=((1,'Fakturowania'), (2,'Dostawy'), (3,'Siedziba')))
    street = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField(blank=True)
    number_room = models.CharField(max_length=10, blank=True)
    postal_code = models.PositiveSmallIntegerField(blank=True, null=True)
    city = models.CharField(max_length=40)
    tax_number = models.IntegerField(unique=True)