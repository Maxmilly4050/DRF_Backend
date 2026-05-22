from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:id>/', views.product_by_id, name='product-by-id'),
    path('orders/', views.order_list, name='order_list')
]
