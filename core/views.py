from django.shortcuts import render
from .models import Menu, Customer, Order, OrderItem, Payment, PaymentChoices, StockIngredient, StaffAssignment, Staff

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
    customers = Customer.objects.all()
    return render(request, 'customer/show_customer.html', {
        'customers': customers
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
    staffs = Staff.objects.all()
    return render(request, 'staff/show_staff.html', {
        'staffs': staffs
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