from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('orders/', views.order_list, name='order_list'),
    path('product_info/', views.product_info, name='product_info'),
    path('silk/', include('silk.urls', namespace='silk'))
]
