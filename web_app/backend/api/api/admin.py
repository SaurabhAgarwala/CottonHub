from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(PhoneOtp)
admin.site.register(CottonType)
admin.site.register(Market)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(OrderItem)
