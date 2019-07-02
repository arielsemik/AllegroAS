from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product, Category, ProductImages
from django.template import loader
from seller.models import Seller, Address

def index(request):
    category_list = "aaasssasasa"
    # category_list = Category.objects.all()
    return render(request, 'products/index.html')

def category_list(request, category_id = None, product_search=None):
    category_list_in = Category.objects.all()
    products = Product.objects.filter(available = True, product_category =category_id)
    if product_search:

        product_search = request.GET['product_search']
        products = Product.objects.filter(available=True, name=product_search, product_category=category_id)

        return render(request, 'products/productlist.html',{"product_search":product_search, "catlist": category_list_in, "products": products, 'category_id':category_id})
    else:
        return render(request, 'products/productlist.html', {"catlist": category_list_in, "products": products, 'category_id': category_id})
def search_products(request, category_id = None, search_input = None):
    category_list_in = Category.objects.all()
    category_id = request.GET['category_id']
    search_prod = request.GET['search_input'].lower().strip()
    if category_id:
        products = Product.objects.filter(available=True, product_category=category_id, name__contains=search_prod)
    else:
        products = Product.objects.filter(available=True, name__contains=search_prod)

    return render(request, 'products/productlist.html', {"catlist": category_list_in, 'category_id':category_id, "product_search": search_prod, "products": products})



def product_list(request, product_id = None):
    category_list_in = Category.objects.all()
    products = Product.objects.filter(available = True)
    us = request.session.get('usersession')


    return render(request, 'products/productlist.html', {'us': us, "catlist":category_list_in, "products": products})


def product_detail(request, product_id):
    #product = get_object_or_404(Product, id=id, available = True)
    #product_image = get_object_or_404(ProductImages, product = id)
    #seller = get_object_or_404(Product, id=id)
    namep = get_object_or_404(Product, id = product_id)
    images   = ProductImages.objects.filter(product=product_id)
    us = request.session.get('usersession')

    return render(request, 'products/productdetails.html', {'price': namep.price,'stock': namep.stock, 'available':namep.available ,'id': product_id, 'productname': namep.name,'description': namep.description, 'images': images, 'us': us})
