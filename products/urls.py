from django.urls import path
from .import views


urlpatterns = [
    path('', views.product_list, name = 'product_list'),
    path('cat'+'<int:category_id>', views.category_list, name='category_list'),
    # path('', views.product_list, name='product_list'),
    path('productdetails/<int:product_id>', views.product_detail, name='product_detail'),
    path('?'+'<str:search_input>', views.category_list, name='search_products'),
]
