from datetime import datetime
from django.shortcuts import redirect, render
from .models import Menu, Customer, Order, OrderItem, Payment, PaymentChoices, StockIngredient, StaffAssignment, Staff

from .forms import CustomerForm, StaffForm, OrderForm, OrderItemForm, StaffAssignmentForm, PaymentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

# menu - ingredient - stocck
def show_menu(request):
    menus = Menu.objects.all()
    return render(request, 'menu/show_menu.html', {
        'menus': menus 
    })

def show_menu_detail(request, menu_id):
    dish = Menu.objects.get(id=menu_id)
    ingredients = dish.ingredients.all()
    return render(request, 'menu/show_ingredient.html', {
        'ingredients': ingredients
    })

def show_stock(request):
    stocks = StockIngredient.objects.all()
    return render(request, 'menu/show_stock.html', {
        'stocks': stocks
    })

def show_stock_detail(request, stock_id):
    stock = StockIngredient.objects.get(id=stock_id)
    related_ingredients = stock.menu_ingredients.all()
    return render(request, 'menu/show_stock_detail.html', {
        'stock': stock, 
        'related_ingredients': related_ingredients
    })

# customer
def show_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    form = CustomerForm()
    customers = Customer.objects.all()
    return render(request, 'customer/show_customer.html', {
        'customers': customers,
        'CustomerForm': form
    })

def show_customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer_orders = customer.customer_orders.all()
    return render(request, 'customer/show_customer_detail.html', {
        'customer': customer,
        'customer_orders': customer_orders
    })

# staff
def show_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
    form = StaffForm()
    staffs = Staff.objects.all()
    return render(request, 'staff/show_staff.html', {
        'staffs': staffs,
        'StaffForm': form
    })

def show_staff_detail(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    # staff2 = staff.assigned_orders.all().first()
    staff_assigneds = staff.assigned_orders.all()
    print(staff_assigneds)
    return render(request, 'staff/show_staff_detail.html', {
        'staff': staff,
        'staff_assigneds': staff_assigneds
    })

# order
def show_order(request):
    orders = Order.objects.all()
    return render(request, 'order/show_order.html', {
        'orders': orders
    })

# Tính năng
def core(request):
    return render(request, 'function/core.html')

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.thoi_gian_dat = datetime.now()
            order.trang_thai = Order.TypeChoices.PENDING
            order.save()
            return redirect('add_dishes', order_id=order.id)
    form = OrderForm()
    return render(request, 'function/create_order.html', {
        'OrderForm': form
    })

def add_dishes(request, order_id):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.order_id = order_id
            order_item.save()
            order_items = OrderItem.objects.filter(order_id=order_id)
            return render(request, 'function/add_dishes.html', {
                'order_id': order_id, 
                'order_items': order_items,
                'form': OrderItemForm()
            })
    order = Order.objects.get(id=order_id)
    form = OrderItemForm()
    return render(request, 'function/add_dishes.html', {
        'order_id': order_id, 
        'order': order,
        'form': form
    })

def assign_staff(request, order_id):
    order = Order.objects.get(id=order_id)
    menu_items = OrderItem.objects.filter(order_id=order_id)
    if request.method == 'POST':
        form = StaffAssignmentForm(request.POST)
        if form.is_valid():
            staff_assignment = form.save(commit=False)
            staff_assignment.order_id = order_id
            staff_assignment.save()
            staffs_assigned = StaffAssignment.objects.filter(order_id=order_id)
            return render(request, 'function/assign_staff.html', {
                'order_id': order_id,
                'staffs_assigned': staffs_assigned,
                'order': order,
                'menu_items': menu_items,
                'form': StaffAssignmentForm()
            })
    form = StaffAssignmentForm()
    return render(request, 'function/assign_staff.html', {
        'order_id': order_id,
        'order': order,
        'menu_items': menu_items,
        'form': form
    })

def payment_check(request, order_id):
    order = Order.objects.get(id=order_id)
    menu_items = OrderItem.objects.filter(order_id=order_id)
    staffs_assigned = StaffAssignment.objects.filter(order_id=order_id)
    customer = order.customer

    total_price = 0
    for item in menu_items:
        total_price += float(item.menu.gia_ban) * float(item.so_luong)
    order.tong_tien = total_price
    order.save()

    form = PaymentForm()

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.tong_tien = total_price
            payment.order = order
            payment.ngay_thanh_toan = datetime.now()
            payment.save()
            order.trang_thai = Order.TypeChoices.COMPLETED
            order.save()
    return render(request, 'function/payment_check.html', {
        'order': order,
        'menu_items': menu_items,
        'staffs_assigned': staffs_assigned,
        'total_price': total_price,
        'customer': customer, 
        'form': form
    })

def show_order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    menu_items = OrderItem.objects.filter(order_id=order_id)
    staffs_assigned = StaffAssignment.objects.filter(order_id=order_id)
    customer = order.customer
    payment = order.order_payment

    return render(request, 'order/show_order_detail.html', {
        'order': order,
        'menu_items': menu_items,
        'staffs_assigned': staffs_assigned,
        'customer': customer,
        'payment': payment
    })