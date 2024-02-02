from django.contrib import admin
from .models import Product, Category, Customer, Cart, Customer_Order, Customer_feedback

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Customer_Order)
admin.site.register(Customer_feedback)
