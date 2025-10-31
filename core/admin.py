from django.contrib import admin
from .models import Menu, MenuIngredient, Customer, StockIngredient, Order, Payment, Staff, StaffAssignment

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuIngredient)
admin.site.register(Customer)
admin.site.register(StockIngredient)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Staff)
admin.site.register(StaffAssignment)
