from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product, Category, ProductImages
from django.template import loader

def index(request):
    category_list = "aaasssasasa"
    # category_list = Category.objects.all()
    return render(request, 'products/index.html')

def category_list(request, category_id = None, search_input = None):

    if search_input:
        products = Product.objects.filter(available = True, name__contains= search_input)
    else:
        products = Product.objects.filter(available = True, product_category =category_id)



    category_list_in = Category.objects.all()
    return render(request, 'products/productlist.html', {"catlist": category_list_in, "product_search": search_input, "products": products})

def product_list(request, product_id = None):
    category_list_in = Category.objects.all()
    products = Product.objects.filter(available = True)
    

    return render(request, 'products/productlist.html', {"catlist":category_list_in, "products": products})


def product_detail(request, product_id):
    #product = get_object_or_404(Product, id=id, available = True)
    #product_image = get_object_or_404(ProductImages, product = id)
    #seller = get_object_or_404(Product, id=id)
    namep = get_object_or_404(Product, id = product_id)
    images   = ProductImages.objects.filter(product=product_id)
    return render(request, 'products/productdetails.html', {'price': namep.price,'stock': namep.stock, 'available':namep.available ,'id': product_id, 'productname': namep.name,'description': namep.description, 'images': images})
        