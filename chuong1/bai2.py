class ThiSinh:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa
    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Lý: {self.diem_ly}")
        print(f"Điểm Hóa: {self.diem_hoa}")
danh_sach_thi_sinh = []
so_luong = int(input("Nhập số lượng thí sinh: "))
for i in range(so_luong):
    ho_ten = input("Nhập họ tên của thí sinh: ")
    diem_toan = float(input("Nhập điểm môn Toán: "))
    diem_ly = float(input("Nhập điểm môn Lý: "))
    diem_hoa = float(input("Nhập điểm môn Hóa: "))
    thi_sinh = ThiSinh(ho_ten, diem_toan, diem_ly, diem_hoa)
    danh_sach_thi_sinh.append(thi_sinh)
print("Danh sách thí sinh trúng tuyển:")
danh_sach_trung_tuyen = []
diem_toi_thieu = 20

for thi_sinh in danh_sach_thi_sinh:
    if thi_sinh.tinh_tong_diem() >= diem_toi_thieu:
        danh_sach_trung_tuyen.append(thi_sinh)
def get_tong_diem(thi_sinh):
    return thi_sinh.tinh_tong_diem()
danh_sach_trung_tuyen.sort(key=get_tong_diem, reverse=True)
for thi_sinh in danh_sach_trung_tuyen:
    thi_sinh.in_thong_tin()
    print("---------------")