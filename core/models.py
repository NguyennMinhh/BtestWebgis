from django.db import models

class Menu(models.Model):
    class TypeChoices(models.TextChoices):
        BURGER = 'Burger'
        DRINK = 'Drink'
        COMBO = 'Combo'
        SNACK = 'Snack'

    ma_mon = models.CharField(max_length=10, unique=True)
    ten_mon = models.CharField(max_length=50)
    loai_mon = models.CharField(max_length=20, choices=TypeChoices.choices)
    gia_ban = models.FloatField()
    don_vi_tinh = models.CharField(max_length=10, default='VND')

    def __str__(self):
        return self.ten_mon

class StockIngredient(models.Model):
    ma_nguyen_lieu = models.CharField(max_length=10, unique=True)
    ten_nguyen_lieu = models.CharField(max_length=50)
    so_luong_ton_kho = models.FloatField()
    chi_phi_nguyen_lieu = models.FloatField()
    nha_cung_cap = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.ten_nguyen_lieu} ({self.so_luong_ton_kho})"


class MenuIngredient(models.Model):
    class TypeChoices(models.TextChoices):
        KILOGRAM = 'Kilogram'
        ITEM = 'Item'

    so_luong = models.FloatField()
    don_vi_tinh = models.CharField(max_length=20, choices=TypeChoices.choices)
    stock = models.ForeignKey(StockIngredient, on_delete=models.CASCADE, related_name='menu_ingredients')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='ingredients')
    def __str__(self):
        return f"{self.stock.ten_nguyen_lieu} dùng cho {self.menu.ten_mon}"


# Demo
class Customer(models.Model):
    class TypeChoices(models.TextChoices):
        NORMAL = 'Normal'
        VIP = 'VIP'
        ONLINE = 'Online'

    ma_khach_hang = models.CharField(max_length=10, unique=True)
    ho_ten = models.CharField(max_length=200)
    so_dien_thoai = models.CharField(max_length=15)
    dia_chi = models.CharField(max_length=200)
    hang_thanh_vien = models.CharField(max_length=20, choices=TypeChoices.choices)

    def __str__(self):
        return f"{self.ho_ten} ({self.hang_thanh_vien})"

class PaymentChoices(models.TextChoices):
    CASH = 'Tiền mặt'
    CREDIT = 'Thẻ tín dụng'

class Order(models.Model):
    class TypeChoices(models.TextChoices):
        PENDING = 'Đang xử lý'
        COMPLETED = 'Đã hoàn thành'
        CANCELED = 'Đã hủy'
    ma_don_hang = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_orders')
    thoi_gian_dat = models.DateTimeField(auto_now_add=True)
    tong_tien = models.FloatField(null=True, blank=True)
    trang_thai = models.CharField(max_length=20, choices=TypeChoices.choices)
    phuong_thuc_thanh_toan = models.CharField(max_length=20, choices=PaymentChoices.choices)

    def __str__(self):
        return f"Đơn hàng {self.ma_don_hang} của {self.customer.ho_ten}"

class Payment(models.Model):
    ma_thanh_toan = models.CharField(max_length=10, unique=True)
    ngay_thanh_toan = models.DateTimeField(auto_now_add=True)
    tong_tien = models.FloatField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_payment')
    phuong_thuc_thanh_toan = models.CharField(max_length=20, choices=PaymentChoices.choices)

    def __str__(self):
        return f"Thanh toán {self.ma_thanh_toan} cho đơn {self.order.ma_don_hang}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='order_items')
    so_luong = models.PositiveIntegerField()

    def __str__(self):
        return f"id: {self.id}, order_id: {self.order.ma_don_hang}, món:{self.menu.ten_mon} x{self.so_luong}"
    
# demo Staff
class Staff(models.Model):
    class JobChoices(models.TextChoices):
        THUNGAN = 'Thu Ngân'
        DAUBEP = 'Đầu Bếp'
        PHUCVU = 'Phục Vụ'
        QUANLY = 'Quản Lý'

    class ShiftChoices(models.TextChoices):
        MORNING = 'Sáng'
        AFTERNOON = 'Chiều'
        NIGHT = 'Tối'
        MIDNIGHT = 'Đêm'

    ma_nhan_vien = models.CharField(max_length=10, unique=True)
    ho_ten = models.CharField(max_length=100)
    chuc_vu = models.CharField(max_length=20, choices=JobChoices.choices)
    so_dien_thoai = models.CharField(max_length=15)
    ca_lam_viec = models.CharField(max_length=20, choices=ShiftChoices.choices)
    def __str__(self):
        return f"{self.ho_ten} - {self.chuc_vu} - "

class StaffAssignment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='assigned_orders')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='assigned_staffs')
    def __str__(self):
        return f"{self.staff.ho_ten} được phân công cho đơn {self.order.ma_don_hang}"

    
