from django.contrib import admin
from .models import Menu, MenuIngredient, Customer, StockIngredient

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuIngredient)
admin.site.register(Customer)
admin.site.register(StockIngredient)
