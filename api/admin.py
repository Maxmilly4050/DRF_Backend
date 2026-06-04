# api/admin.py
from django.contrib import admin
from .models import User, Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]

admin.site.register(User)
# admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
