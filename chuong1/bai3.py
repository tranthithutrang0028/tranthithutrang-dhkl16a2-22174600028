class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        while True:
            self.mau_so = int(input("Nhập mẫu số (khác 0): "))
            if self.kiem_tra_hop_le():
                break
            else:
                print("Mẫu số không hợp lệ. Vui lòng nhập lại.")

    def in_phan_so(self):
        print(f"Phân số: {self.tu_so}/{self.mau_so}")
ps = PhanSo(5,4)
ps.nhap_phan_so()
ps.in_phan_so()
