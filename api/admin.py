# api/admin.py
from django.contrib import admin
from .models import User, Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock')  # Show these fields in the list view
    search_fields = ('name',)  # Add search functionality

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')  # Add filters

admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
