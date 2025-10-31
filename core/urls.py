from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Menu
    path('menu/', views.show_menu, name='show_menu'),
    path('menu/<int:menu_id>', views.show_menu_detail, name='show_menu_detail'),
    path('stock/', views.show_stock, name='show_stock'),
    path('stock/<int:stock_id>', views.show_stock_detail, name='show_stock_detail'),

    # Customer
    path('customer/', views.show_customer, name='show_customer'),
    path('customer/<int:customer_id>', views.show_customer_detail, name='show_customer_detail'),

    # Order
    path('order/', views.show_order, name='show_order'),
]