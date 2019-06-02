from django.contrib import admin
from .models import Seller, Address

class SellerAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'description', 'email', 'password']
admin.site.register(Seller, SellerAdmin )

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_type','street','number', 'number_room', 'postal_code', 'city','tax_number']
admin.site.register(Address, AddressAdmin)
