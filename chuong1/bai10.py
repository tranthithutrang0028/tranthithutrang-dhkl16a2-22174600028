import math

class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def tinh_dien_tich(self):
        return math.pi * self.a * self.b

class DuongTron(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)  # Đường tròn là elip có bán kính a = b = r

# Nhập thông tin cho elip
x_elip = float(input("Nhập hoành độ của điểm trung tâm elip: "))
y_elip = float(input("Nhập tung độ của điểm trung tâm elip: "))
a_elip = float(input("Nhập chiều dài trục lớn elip: "))
b_elip = float(input("Nhập chiều dài trục nhỏ elip: "))

# Tạo đối tượng elip
elip = Elip(x_elip, y_elip, a_elip, b_elip)

# In diện tích của elip
print(f"Diện tích của elip: {elip.tinh_dien_tich()}")

# Nhập thông tin cho đường tròn (đường tròn là trường hợp đặc biệt của elip)
x_duong_tron = float(input("Nhập hoành độ của điểm trung tâm đường tròn: "))
y_duong_tron = float(input("Nhập tung độ của điểm trung tâm đường tròn: "))
r_duong_tron = float(input("Nhập bán kính đường tròn: "))

# Tạo đối tượng đường tròn
duong_tron = DuongTron(x_duong_tron, y_duong_tron, r_duong_tron)

# In diện tích của đường tròn
print(f"Diện tích của đường tròn: {duong_tron.tinh_dien_tich()}")
