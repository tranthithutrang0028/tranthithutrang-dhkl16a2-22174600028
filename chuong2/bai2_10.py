import json
from datetime import datetime

def ghi_giao_dich_vao_tap_tin(giao_dich):
    # Lấy thông tin ngày hiện tại
    ngay_hien_tai = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Tạo tên tập tin dựa trên thông tin ngày
    ten_tap_tin = f"{ngay_hien_tai}.json"

    # Lưu danh sách giao dịch vào tập tin JSON
    with open(ten_tap_tin, "w") as file:
        json.dump(giao_dich, file)

    print(f"Ghi thành công vào tập tin: {ten_tap_tin}")

def quan_ly_giao_dich():
    giao_dich = []

    while True:
        print("1. Thêm giao dịch")
        print("2. Hiển thị danh sách giao dịch")
        print("0. Kết thúc")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            # Mô phỏng thêm giao dịch
            loai_giao_dich = input("Nhập loại giao dịch (Tiền/Vàng): ")
            so_luong = float(input("Nhập số lượng: "))
            gia = float(input("Nhập giá: "))

            giao_dich.append({
                "Loai": loai_giao_dich,
                "SoLuong": so_luong,
                "Gia": gia
            })
        elif lua_chon == "2":
            # Hiển thị danh sách giao dịch
            print("Danh sách giao dịch:")
            for gd in giao_dich:
                print(f"Loại: {gd['Loai']}, Số lượng: {gd['SoLuong']}, Giá: {gd['Gia']}")

        elif lua_chon == "0":
            # Yêu cầu người dùng có muốn ghi vào tập tin hay không
            ghi_tap_tin = input("Bạn có muốn ghi vào tập tin không? (1: Có, 0: Không): ")

            if ghi_tap_tin == "1":
                ghi_giao_dich_vao_tap_tin(giao_dich)
            
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

# Gọi hàm quản lý giao dịch
quan_ly_giao_dich()
