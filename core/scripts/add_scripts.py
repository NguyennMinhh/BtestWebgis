from core.models import Menu, StockIngredient, MenuIngredient, Customer, Order, Payment, PaymentChoices
from django.utils import timezone

def run():

    Menu.objects.all().delete()
    StockIngredient.objects.all().delete()
    MenuIngredient.objects.all().delete()
    Customer.objects.all().delete()
    Order.objects.all().delete()
    Payment.objects.all().delete()

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
    cus1 = Customer.objects.create(
        ma_khach_hang='CUS01',
        ho_ten='Nguyễn Văn A',
        so_dien_thoai='0901234567',
        dia_chi='Hà Nội',
        hang_thanh_vien=Customer.TypeChoices.NORMAL
    )
    cus2 = Customer.objects.create(
        ma_khach_hang='CUS02',
        ho_ten='Trần Thị B',
        so_dien_thoai='0907654321',
        dia_chi='Hồ Chí Minh',
        hang_thanh_vien=Customer.TypeChoices.VIP
    )

    # ----- Tạo đơn hàng mẫu -----
    order1 = Order.objects.create(
        ma_don_hang='ORD01',
        customer=cus1,
        tong_tien=menu1.gia_ban + menu3.gia_ban,
        trang_thai=Order.TypeChoices.COMPLETED,
        phuong_thuc_thanh_toan=PaymentChoices.CASH
    )

    order2 = Order.objects.create(
        ma_don_hang='ORD02',
        customer=cus2,
        tong_tien=menu2.gia_ban * 2,
        trang_thai=Order.TypeChoices.PENDING,
        phuong_thuc_thanh_toan=PaymentChoices.CREDIT
    )

    # ----- Tạo thanh toán mẫu -----
    Payment.objects.create(
        ma_thanh_toan='PAY01',
        ngay_thanh_toan=timezone.now(),
        tong_tien=order1.tong_tien,
        order=order1,
        phuong_thuc_thanh_toan=PaymentChoices.CASH
    )

    Payment.objects.create(
        ma_thanh_toan='PAY02',
        ngay_thanh_toan=timezone.now(),
        tong_tien=order2.tong_tien,
        order=order2,
        phuong_thuc_thanh_toan=PaymentChoices.CREDIT
    )

    print("Dữ liệu mẫu (Menu, Kho, Khách hàng, Đơn hàng, Thanh toán) đã được tạo thành công.")
