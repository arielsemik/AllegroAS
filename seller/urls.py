from django.urls import path
from . import views

urlpatterns = [
    path('singup/', views.sing_up, name='sing_up'),
    path('singup/submit/', views.submit, name='submit'),
    path('singin/', views.sing_in, name='sing_in'),
    path('', views.login, name='login'),
    path('products/', views.seller_products, name='seller_products'),
    path('menu/', views.selle_menu, name='seller_menu'),
    path('logouta/', views.logouta, name='logouta'),

]
