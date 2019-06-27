from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('singup/', views.sing_up, name='sing_up'),
    path('singup/submit/', views.submit, name='submit'),
    path('singin/', views.sing_in, name='sing_in'),
    path('menu/', views.seller_menu, name='seller_menu'),
    path('products/', views.seller_products, name='seller_products'),
]
