class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh
        self.canh = []

    def nhap_canh(self):
        print(f"Nhập độ dài các cạnh của đa giác ({self.so_canh} cạnh):")
        for i in range(self.so_canh):
            do_dai = float(input(f"Độ dài cạnh {i + 1}: "))
            self.canh.append(do_dai)

    def hien_thi_thong_tin(self):
        print(f"Đa giác có {self.so_canh} cạnh với độ dài các cạnh là: {self.canh}")


class HinhBinhHanh(DaGiac):
    def __init__(self):
        super().__init__(4) #hbh 4 cạnh
        self.do_dai_day = 0
        self.chieu_cao = 0

    def nhap_kich_thuoc(self):
        self.do_dai_day = float(input("Nhập độ dài cạnh đáy của hình bình hành: "))
        self.chieu_cao = float(input("Nhập chiều cao của hình bình hành: "))

    def tinh_dien_tich(self):
        return self.do_dai_day * self.chieu_cao

    def tinh_chu_vi(self):
        return 2 * (self.do_dai_day + sum(self.canh))


class HinhChuNhat(HinhBinhHanh):
    def __init__(self):
        super().__init__()

    def tinh_dien_tich(self):
        return self.do_dai_day * self.chieu_cao

    def tinh_chu_vi(self):
        return 2 * (self.do_dai_day + sum(self.canh))


class HinhVuong(HinhChuNhat):
    def __init__(self):
        super().__init__()

    def tinh_dien_tich(self):
        return self.do_dai_day * self.do_dai_day

    def tinh_chu_vi(self):
        return 4 * self.do_dai_day


hinh_binh_hanh = HinhBinhHanh()
hinh_binh_hanh.nhap_kich_thuoc()

# In ra màn hình chu vi và diện tích của hình bình hành
print("\nThông tin hình bình hành:")
print(f"Chu vi: {hinh_binh_hanh.tinh_chu_vi()}")
print(f"Diện tích: {hinh_binh_hanh.tinh_dien_tich()}")

hinh_chu_nhat = HinhChuNhat()
hinh_chu_nhat.nhap_kich_thuoc()

# In ra màn hình chu vi và diện tích của hình chữ nhật
print("\nThông tin hình chữ nhật:")
print(f"Chu vi: {hinh_chu_nhat.tinh_chu_vi()}")
print(f"Diện tích: {hinh_chu_nhat.tinh_dien_tich()}")

hinh_vuong = HinhVuong()
hinh_vuong.nhap_kich_thuoc()

# In ra màn hình chu vi và diện tích của hình vuông
print("\nThông tin hình vuông:")
print(f"Chu vi: {hinh_vuong.tinh_chu_vi()}")
print(f"Diện tích: {hinh_vuong.tinh_dien_tich()}")

