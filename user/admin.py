from django.contrib import admin
from api.models import (Cart ,Category, Order, Product, ShippingAddress,
                         Seller, Review, OrderItem, CartItem, 
                         AboutUs, ProductImage, Contact, Color, Size, Style)


# Register your models here. 

admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(Seller)
admin.site.register(Review)
admin.site.register(OrderItem)
admin.site.register(CartItem)
admin.site.register(AboutUs)
admin.site.register(ProductImage)
admin.site.register(Contact)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Style)