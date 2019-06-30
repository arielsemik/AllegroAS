from django.urls import path
from . import views

urlpatterns = [
    path('singup/', views.sing_up, name='sing_up'),
    path('singup/submit/', views.submit, name='submit'),
    path('singin/', views.sing_in, name='sing_in'),
    path('', views.seller_menu, name='seller_menu'),
    # path('<str:email>', views.seller_menu2, name='seller_menu2'),
    path('products/', views.seller_products, name='seller_products'),
]
