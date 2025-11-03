from django import forms
from .models import Menu, StockIngredient, MenuIngredient, Customer, PaymentChoices, Order, Payment, OrderItem, Staff, StaffAssignment

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['ma_khach_hang', 'ho_ten', 'so_dien_thoai', 'dia_chi', 'hang_thanh_vien']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['ma_nhan_vien', 'ho_ten', 'chuc_vu', 'so_dien_thoai', 'ca_lam_viec']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['ma_don_hang', 'customer', 'phuong_thuc_thanh_toan']

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu', 'so_luong']

class StaffAssignmentForm(forms.ModelForm):
    class Meta:
        model = StaffAssignment
        fields = ['staff']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['ma_thanh_toan', 'phuong_thuc_thanh_toan']
