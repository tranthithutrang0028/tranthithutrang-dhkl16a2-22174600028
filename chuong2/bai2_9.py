import json

# Dữ liệu JSON mẫu
json_data = '''
{
    "ten_cong_ty": "Công ty TNHH Đất Việt",
    "dia_chi": "abc Giải Phóng – Hà Nội",
    "tong_so_nhan_vien": 100,
    "don_vi": [
        {"ten_don_vi": "Đơn vị A1", "so_nhan_vien":100},
        {"ten_don_vi": "Đơn vị A2", "so_nhan_vien":200},
        {"ten_don_vi": "Đơn vị A3", "so_nhan_vien":300},
        {"ten_don_vi": "Đơn vị A4", "so_nhan_vien":400},
        {"ten_don_vi": "Đơn vị A5", "so_nhan_vien":500}
    ]
}
'''

def thong_ke_nhan_vien(json_data):
    # Đọc dữ liệu từ JSON
    data = json.loads(json_data)

    # In thông tin công ty
    print("Tên công ty:", data["ten_cong_ty"])
    print("Địa chỉ:", data["dia_chi"])

    # Tổng số nhân viên
    tong_so_nhan_vien = 0

    # Thống kê nhân viên theo đơn vị
    for i, don_vi in enumerate(data["don_vi"]):
        ten_don_vi = don_vi["ten_don_vi"]
        so_nhan_vien = don_vi["so_nhan_vien"]
        ty_le = (so_nhan_vien / data["tong_so_nhan_vien"]) * 100

        print(f"{i+1}./ Tên đơn vị: {ten_don_vi}.")
        print(f"   - Số nhân viên: {so_nhan_vien}.")
        print(f"   - Tỷ lệ: {ty_le:.2f}%.")
        print()

        # Tính tổng số nhân viên
        tong_so_nhan_vien += so_nhan_vien

    # In tổng số nhân viên
    print("Tổng số nhân viên:", tong_so_nhan_vien)

# Gọi hàm thống kê nhân viên
thong_ke_nhan_vien(json_data)
