from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.urls import *
from django.core.mail import send_mail
from products import models
from products.models import Product, Category, ProductImages


def index(request):
    pass

def sing_up(request):
     return render(request, 'seller/singup.html')

def submit(request):
    error = False
    error_msg =''

    if len(request.POST['email']) == 0:
        error = True
        error_msg += 'Nie wypelniłeś pola email \n\n\n'

    if error:
        return render(request, 'seller/singup.html', {'invalid_form': error_msg, 'fields': request.POST})
    else:
        massage = Seller(
            company_name =request.POST['companyname'],
            email = request.POST['email'],
            password =request.POST['password']
        )
        massage.save()
        company_name = request.POST['companyname']
        return render(request, 'seller/submit.html', {'company': company_name}) # lub użyć redirect aby przeniosłop na inny adres

def sing_in(request):
    return render(request, 'seller/singin.html')

def seller_menu(request):
    # Wysyla email i hasło, sprawdza czy jest w bazie
    error = False
    error_msg =''
    email = request.POST['email']
    user = Seller.objects.filter(email=email)[0] #uzyc getobjector404

    haslo = request.POST['password']


    if (user.email)[0] == None:
        error = True
        error_msg = 'Brak Ciebie w bazie danych'

    elif user.password != haslo:
        error = True
        error_msg = 'Blędne hasło'


    if error:
        return render(request, 'seller/singin.html', {'invalid_form': error_msg, 'fields': request.POST})
    else:
        return render(request, 'seller/seller_menu.html', {'seller': user, 'email': email})


def seller_products(request):
    email = request.POST['email']
    user = Seller.objects.filter(email=email)[0] #uzyc getobjector404


    return render(request, 'seller/seller_products.html',{"products": products})






