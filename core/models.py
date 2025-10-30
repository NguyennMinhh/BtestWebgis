from django.db import models

class Menu(models.Model):
    class TypeChoices(models.TextChoices):
        BURGER = 'BUR', 'Burger'
        DRINK = 'DRN', 'Drink'
        COMBO = 'CMB', 'Combo'
        SNACK = 'SNK', 'Snack'

    ma_mon = models.CharField(max_length=10, unique=True)
    ten_mon = models.CharField(max_length=50)
    loai_mon = models.CharField(max_length=3, choices=TypeChoices.choices)
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
        KILOGRAM = 'KG', 'Kilogram'
        ITEM = 'IT', 'Item'

    so_luong = models.FloatField()
    don_vi_tinh = models.CharField(max_length=2, choices=TypeChoices.choices)
    stock = models.ForeignKey(StockIngredient, on_delete=models.CASCADE, related_name='stock')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu')
    def __str__(self):
        return f"{self.stock.ten_nguyen_lieu} dùng cho {self.menu.ten_mon}"


class Customer(models.Model):
    class TypeChoices(models.TextChoices):
        NORMAL = 'NRM', 'Normal'
        VIP = 'VIP', 'VIP'
        ONLINE = 'ONL', 'Online'

    ma_khach_hang = models.CharField(max_length=10, unique=True)
    ho_ten = models.CharField(max_length=200)
    so_dien_thoai = models.CharField(max_length=15)
    dia_chi = models.CharField(max_length=200)
    hang_thanh_vien = models.CharField(max_length=3, choices=TypeChoices.choices)

    def __str__(self):
        return self.ho_ten
