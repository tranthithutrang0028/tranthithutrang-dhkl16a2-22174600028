class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
        self.chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    def in_thong_tin(self): 
        print("Chiều dài hình chữ nhật: ", self.chieu_dai)
        print("Chiều rộng hình chữ nhật: ", self.chieu_rong)
        print("Chu vi hình chữ nhật: ", self.tinh_chu_vi())
        print("Diện tích hình chữ nhật: ", self.tinh_dien_tich())
hcn=HinhChuNhat(5,4)
hcn.nhap_du_lieu()
hcn.in_thong_tin()