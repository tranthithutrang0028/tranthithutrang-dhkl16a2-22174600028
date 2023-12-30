class Stack:
    def __init__(self, kt_toi_da):
        self.kt_toi_da = kt_toi_da
        self.stack = []

    def push(self,them):
        if len(self.stack) < self.kt_toi_da:
            self.stack.append(them)
            print(f"{them} push to stack")
        else:
            print("Stack đã đầy")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack đang trống không xóa được!!")

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.kt_toi_da
    def count(self):
        return len(self.stack)
    def __del__(self):
        del self.stack

# Sử dụng lớp Stack
stack = Stack(3)#Lớp stack có 3 ngăn
stack.push(5)
stack.push(4)
stack.push(2)
stack.push(9)# Stack đã đầy
print("Số lượng phần tử trên ngăn xếp:", stack.count())
print(stack.pop())  #del 2
print(stack.pop())  #del 4
print(stack.pop())  #del 5
print("Số lượng phần tử trên ngăn xếp:", stack.count())
print(stack.isEmpty())  # True
print(stack.isFull())  # False
