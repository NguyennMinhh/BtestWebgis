from django.urls import path, include
from . import views

urlpatterns = [
    # Menu
    path('menu/', views.show_menu, name='show_menu'),
    path('menu/<int:menu_id>', views.show_menu_detail, name='show_menu_detail'),
    path('stock/', views.show_stock, name='show_stock'),
    path('stock/<int:stock_id>', views.show_stock_detail, name='show_stock_detail'),

    # Customer
    path('customer/', views.show_customer, name='show_customer'),
    path('customer/<int:customer_id>', views.show_customer_detail, name='show_customer_detail'),

    # Staff
    path('staff/', views.show_staff, name='show_staff'),
    path('staff/<int:staff_id>', views.show_staff_detail, name='show_staff_detail'),

    # Order
    path('order/', views.show_order, name='show_order'),
    path('order/<int:order_id>', views.show_order_detail, name='show_order_detail'),

    # Report
    path('report/', views.report, name='report'),

    # Tính năng
    path('', views.core, name='core'),
    # path('core/create/', views.create, name='create'),
    path('create/order', views.create_order, name='create_order'),
    path('create/order/<int:order_id>/', views.add_dishes, name='add_dishes'),
    path('create/order/<int:order_id>/staff/', views.assign_staff, name='assign_staff'),
    path('create/order/<int:order_id>/staff/payment/', views.payment_check, name='payment_check'),
]