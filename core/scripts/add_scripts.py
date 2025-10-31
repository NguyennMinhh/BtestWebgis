from core.models import (
    Menu, StockIngredient, MenuIngredient,
    Customer, Order, Payment, PaymentChoices,
    OrderItem, Staff, StaffAssignment
)
from django.utils import timezone


def run():
    # Xóa toàn bộ dữ liệu cũ
    Menu.objects.all().delete()
    StockIngredient.objects.all().delete()
    MenuIngredient.objects.all().delete()
    Customer.objects.all().delete()
    Order.objects.all().delete()
    Payment.objects.all().delete()
    OrderItem.objects.all().delete()
    Staff.objects.all().delete()
    StaffAssignment.objects.all().delete()

    # ----- Tạo Menu -----
    menu1 = Menu.objects.create(ma_mon='BUR01', ten_mon='Burger Gà', loai_mon=Menu.TypeChoices.BURGER, gia_ban=30000)
    menu2 = Menu.objects.create(ma_mon='BUR02', ten_mon='Burger Lợn', loai_mon=Menu.TypeChoices.BURGER, gia_ban=25000)
    menu3 = Menu.objects.create(ma_mon='DRN01', ten_mon='Coca', loai_mon=Menu.TypeChoices.DRINK, gia_ban=10000)
    menu4 = Menu.objects.create(ma_mon='SNK01', ten_mon='Khoai Tây Chiên', loai_mon=Menu.TypeChoices.SNACK, gia_ban=15000)

    # ----- Tạo nguyên liệu -----
    chicken = StockIngredient.objects.create(ma_nguyen_lieu='ING01', ten_nguyen_lieu='Thịt gà', so_luong_ton_kho=20, chi_phi_nguyen_lieu=50000, nha_cung_cap='MeatCP')
    pork = StockIngredient.objects.create(ma_nguyen_lieu='ING02', ten_nguyen_lieu='Thịt lợn', so_luong_ton_kho=30, chi_phi_nguyen_lieu=60000, nha_cung_cap='MeatCP')
    water = StockIngredient.objects.create(ma_nguyen_lieu='ING03', ten_nguyen_lieu='Nước lọc chai', so_luong_ton_kho=50, chi_phi_nguyen_lieu=5000, nha_cung_cap='AquaViet')
    bread = StockIngredient.objects.create(ma_nguyen_lieu='ING04', ten_nguyen_lieu='Bánh mì', so_luong_ton_kho=150, chi_phi_nguyen_lieu=5000, nha_cung_cap='BakeCP')
    potato = StockIngredient.objects.create(ma_nguyen_lieu='ING05', ten_nguyen_lieu='Khoai tây', so_luong_ton_kho=100, chi_phi_nguyen_lieu=8000, nha_cung_cap='FarmVN')

    # ----- Liên kết món với nguyên liệu -----
    MenuIngredient.objects.create(stock=chicken, menu=menu1, so_luong=0.5, don_vi_tinh=MenuIngredient.TypeChoices.KILOGRAM)
    MenuIngredient.objects.create(stock=bread, menu=menu1, so_luong=1, don_vi_tinh=MenuIngredient.TypeChoices.ITEM)
    MenuIngredient.objects.create(stock=pork, menu=menu2, so_luong=0.5, don_vi_tinh=MenuIngredient.TypeChoices.KILOGRAM)
    MenuIngredient.objects.create(stock=bread, menu=menu2, so_luong=1, don_vi_tinh=MenuIngredient.TypeChoices.ITEM)
    MenuIngredient.objects.create(stock=water, menu=menu3, so_luong=1, don_vi_tinh=MenuIngredient.TypeChoices.ITEM)
    MenuIngredient.objects.create(stock=potato, menu=menu4, so_luong=0.3, don_vi_tinh=MenuIngredient.TypeChoices.KILOGRAM)

    # ----- Tạo khách hàng -----
    cus1 = Customer.objects.create(ma_khach_hang='CUS01', ho_ten='Nguyễn Văn A', so_dien_thoai='0901234567', dia_chi='Hà Nội', hang_thanh_vien=Customer.TypeChoices.NORMAL)
    cus2 = Customer.objects.create(ma_khach_hang='CUS02', ho_ten='Trần Thị B', so_dien_thoai='0907654321', dia_chi='Hồ Chí Minh', hang_thanh_vien=Customer.TypeChoices.VIP)
    cus3 = Customer.objects.create(ma_khach_hang='CUS03', ho_ten='Lê Quốc C', so_dien_thoai='0912345678', dia_chi='Đà Nẵng', hang_thanh_vien=Customer.TypeChoices.ONLINE)

    # ----- Tạo đơn hàng -----
    order1 = Order.objects.create(ma_don_hang='ORD01', customer=cus1, tong_tien=menu1.gia_ban + menu3.gia_ban, trang_thai=Order.TypeChoices.COMPLETED, phuong_thuc_thanh_toan=PaymentChoices.CASH)
    order2 = Order.objects.create(ma_don_hang='ORD02', customer=cus2, tong_tien=menu2.gia_ban * 2 + menu4.gia_ban, trang_thai=Order.TypeChoices.PENDING, phuong_thuc_thanh_toan=PaymentChoices.CREDIT)
    order3 = Order.objects.create(ma_don_hang='ORD03', customer=cus3, tong_tien=menu1.gia_ban + menu2.gia_ban + menu3.gia_ban, trang_thai=Order.TypeChoices.CANCELED, phuong_thuc_thanh_toan=PaymentChoices.CASH)

    # ----- Tạo OrderItem -----
    OrderItem.objects.create(order=order1, menu=menu1, so_luong=1)
    OrderItem.objects.create(order=order1, menu=menu3, so_luong=1)
    OrderItem.objects.create(order=order2, menu=menu2, so_luong=2)
    OrderItem.objects.create(order=order2, menu=menu4, so_luong=1)
    OrderItem.objects.create(order=order3, menu=menu1, so_luong=1)
    OrderItem.objects.create(order=order3, menu=menu2, so_luong=1)
    OrderItem.objects.create(order=order3, menu=menu3, so_luong=1)

    # ----- Tạo thanh toán -----
    Payment.objects.create(ma_thanh_toan='PAY01', ngay_thanh_toan=timezone.now(), tong_tien=order1.tong_tien, order=order1, phuong_thuc_thanh_toan=PaymentChoices.CASH)
    Payment.objects.create(ma_thanh_toan='PAY02', ngay_thanh_toan=timezone.now(), tong_tien=order2.tong_tien, order=order2, phuong_thuc_thanh_toan=PaymentChoices.CREDIT)

    # ----- Tạo nhân viên -----
    staff1 = Staff.objects.create(ma_nhan_vien='ST01', ho_ten='Phạm Thu Ngân', chuc_vu=Staff.JobChoices.THUNGAN, so_dien_thoai='0988123456', ca_lam_viec=Staff.ShiftChoices.MORNING)
    staff2 = Staff.objects.create(ma_nhan_vien='ST02', ho_ten='Lê Văn Bếp', chuc_vu=Staff.JobChoices.DAUBEP, so_dien_thoai='0977456123', ca_lam_viec=Staff.ShiftChoices.AFTERNOON)
    staff3 = Staff.objects.create(ma_nhan_vien='ST03', ho_ten='Ngô Hữu Phục', chuc_vu=Staff.JobChoices.PHUCVU, so_dien_thoai='0967333222', ca_lam_viec=Staff.ShiftChoices.NIGHT)
    staff4 = Staff.objects.create(ma_nhan_vien='ST04', ho_ten='Nguyễn Quản Lý', chuc_vu=Staff.JobChoices.QUANLY, so_dien_thoai='0959000111', ca_lam_viec=Staff.ShiftChoices.MORNING)

    # ----- Phân công nhân viên vào đơn hàng -----
    StaffAssignment.objects.create(staff=staff1, order=order1)
    StaffAssignment.objects.create(staff=staff2, order=order1)
    StaffAssignment.objects.create(staff=staff3, order=order2)
    StaffAssignment.objects.create(staff=staff4, order=order2)
    StaffAssignment.objects.create(staff=staff1, order=order3)
    StaffAssignment.objects.create(staff=staff2, order=order3)

    print("✅ Dữ liệu mẫu (Menu, Kho, Khách hàng, Đơn hàng, Món, Thanh toán, Nhân viên, Phân công) đã được tạo thành công.")
