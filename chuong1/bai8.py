class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Ngày: {self.day}/{self.month}/{self.year}")

    def next(self):
        # Kiểm tra ngày
        if self.day == 31 and self.month in [1, 3, 5, 7, 8, 10, 12]:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        elif self.day == 30 and self.month in [4, 6, 9, 11]:
            self.day = 1
            self.month += 1
        # Kiểm tra ngày tháng 2
        elif self.day == 28 and self.month == 2:
            if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
                self.day += 1
            else:
                self.day = 1
                self.month += 1
        # Trường hợp còn lại
        else:
            self.day += 1
class Employee(Date):  # Kế thừa từ lớp Date
    def __init__(self, full_name, birth_date, hire_date):
        super().__init__(birth_date.day, birth_date.month, birth_date.year)
        self.full_name = full_name
        self.hire_date = hire_date

    def display_info(self):
        print(f"Họ tên: {self.full_name}")
        print("Ngày sinh:")
        self.display()  # Gọi phương thức display của lớp Date
        print("Ngày vào công ty:")
        self.hire_date.display()
birth_date = Date(15, 5, 1990)
hire_date = Date(1,10, 2023)

employee = Employee("Nguyen Van A", birth_date, hire_date)
employee.display_info() 
