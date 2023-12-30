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
date = Date(31, 12, 2025)
date.display()  
date.next()  
date.display()  
