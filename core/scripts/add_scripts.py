from core.models import Menu, StockIngredient, MenuIngredient, Customer
from django.utils import timezone

def run():
    # ----- Tạo Menu -----
    menu1 = Menu.objects.create(
        ma_mon='BUR01',
        ten_mon='Burger Gà',
        loai_mon=Menu.TypeChoices.BURGER,
        gia_ban=30000,
    )
    menu2 = Menu.objects.create(
        ma_mon='BUR02',
        ten_mon='Burger Lợn',
        loai_mon=Menu.TypeChoices.BURGER,
        gia_ban=25000,
    )
    menu3 = Menu.objects.create(
        ma_mon='DRN01',
        ten_mon='Coca',
        loai_mon=Menu.TypeChoices.DRINK,
        gia_ban=10000,
    )

    # ----- Tạo nguyên liệu trong kho -----
    chicken = StockIngredient.objects.create(
        ma_nguyen_lieu='ING01',
        ten_nguyen_lieu='Thịt gà',
        so_luong_ton_kho=20,
        chi_phi_nguyen_lieu=50000,
        nha_cung_cap='MeatCP'
    )

    pork = StockIngredient.objects.create(
        ma_nguyen_lieu='ING02',
        ten_nguyen_lieu='Thịt lợn',
        so_luong_ton_kho=30,
        chi_phi_nguyen_lieu=60000,
        nha_cung_cap='MeatCP'
    )

    water = StockIngredient.objects.create(
        ma_nguyen_lieu='ING03',
        ten_nguyen_lieu='Nước lọc chai',
        so_luong_ton_kho=50,
        chi_phi_nguyen_lieu=5000,
        nha_cung_cap='AquaViet'
    )

    bread = StockIngredient.objects.create(
        ma_nguyen_lieu='ING04',
        ten_nguyen_lieu='Bánh mì',
        so_luong_ton_kho=150,
        chi_phi_nguyen_lieu=5000,
        nha_cung_cap='BakeCP'
    )

    # ----- Liên kết món với nguyên liệu -----
    MenuIngredient.objects.create(
        stock=chicken,
        menu=menu1,
        so_luong=0.5,
        don_vi_tinh=MenuIngredient.TypeChoices.KILOGRAM
    )

    MenuIngredient.objects.create(
        stock=bread,
        menu=menu1,
        so_luong=1,
        don_vi_tinh=MenuIngredient.TypeChoices.ITEM
    )

    MenuIngredient.objects.create(
        stock=bread,
        menu=menu2,
        so_luong=1,
        don_vi_tinh=MenuIngredient.TypeChoices.ITEM
    )

    MenuIngredient.objects.create(
        stock=pork,
        menu=menu2,
        so_luong=0.5,
        don_vi_tinh=MenuIngredient.TypeChoices.KILOGRAM
    )

    MenuIngredient.objects.create(
        stock=water,
        menu=menu3,
        so_luong=1,
        don_vi_tinh=MenuIngredient.TypeChoices.ITEM
    )

    # ----- Tạo khách hàng mẫu -----
    Customer.objects.create(
        ma_khach_hang='CUS01',
        ho_ten='Nguyễn Văn A',
        so_dien_thoai='0901234567',
        dia_chi='Hà Nội',
        hang_thanh_vien=Customer.TypeChoices.NORMAL
    )

    Customer.objects.create(
        ma_khach_hang='CUS02',
        ho_ten='Trần Thị B',
        so_dien_thoai='0907654321',
        dia_chi='Hồ Chí Minh',
        hang_thanh_vien=Customer.TypeChoices.VIP
    )

    print("Dữ liệu mẫu đã được tạo thành công.")
