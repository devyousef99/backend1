from django.contrib import admin
from .models import *
from product.models import *
from order.models import *
# Register your models here.

admin.site.register(Type)
admin.site.register(Store)
admin.site.register(Usr)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Color)