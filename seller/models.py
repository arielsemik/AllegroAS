from django.db import models

# Create your models here.
from django.db import models

class Seller(models.Model):
    company_name = models.CharField(max_length=200,verbose_name='Nazwa firmy')
    description = models.CharField(max_length=1000, null=True, blank= True, verbose_name='Opis firmy')
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    password = models.CharField(max_length=40, verbose_name='Hasło')
    def __str__(self):
        return self.company_name



class Address(models.Model):
    company = models.ForeignKey(Seller, on_delete=models.CASCADE, default=None)
    address_type = models.CharField(max_length=40, choices=((1,'Fakturowania'), (2,'Dostawy'), (3,'Siedziba')))
    street = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField(blank=True)
    number_room = models.CharField(max_length=10, blank=True)
    postal_code = models.PositiveSmallIntegerField(blank=True, null=True)
    city = models.CharField(max_length=40)
    tax_number = models.IntegerField(unique=True)
