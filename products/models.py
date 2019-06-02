from django.db import models
from datetime import *
from seller.models import Seller


class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Kategoria')
    cat_name_father = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                        verbose_name='Kategoria nadrzędna')
    level = models.PositiveSmallIntegerField(default=0, verbose_name='Poziom kategorii')

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nazwa produktu')
    description = models.CharField(max_length=4000, verbose_name='Opis', blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Kategoria produktu')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cena')
    stock = models.PositiveIntegerField(default=0, verbose_name='Dostępna ilość')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Sprzedawca')

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Nazwa produktu')
    image = models.ImageField(upload_to='products/images/', blank=True)
    created = models.DateTimeField(auto_now_add=True)

#  def __str__(self):
#     return ("img-{}-{}".format(self.product, self.id))