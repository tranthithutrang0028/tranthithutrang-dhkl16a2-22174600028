import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinh_chu_vi(self):
        return self.a + self.b + self.c

    def tinh_dien_tich(self):
        s = self.tinh_chu_vi() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class TamGiacVuong(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def la_tam_giac_vuong(self):
        canh = sorted([self.a, self.b, self.c])
        return canh[0]**2 + canh[1]**2 == canh[2]**2

class TamGiacCan(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def la_tam_giac_can(self):
        return self.a == self.b or self.b == self.c or self.c == self.a

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a, a)

# Sử dụng ví dụ:
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

tam_giac = TamGiac(a, b, c)
print(f"Chu vi tam giác: {tam_giac.tinh_chu_vi()}")
print(f"Diện tích tam giác: {tam_giac.tinh_dien_tich()}")

tam_giac_vuong = TamGiacVuong(a, b, c)
if tam_giac_vuong.la_tam_giac_vuong():
    print("Tam giác này là tam giác vuông.")
else:
    print("Tam giác này không phải là tam giác vuông.")

tam_giac_can = TamGiacCan(a, b, c)
if tam_giac_can.la_tam_giac_can():
    print("Tam giác này là tam giác cân.")
else:
    print("Tam giác này không phải là tam giác cân.")

tam_giac_deu = TamGiacDeu(a)
print(f"Chu vi tam giác đều: {tam_giac_deu.tinh_chu_vi()}")
print(f"Diện tích tam giác đều: {tam_giac_deu.tinh_dien_tich()}")
