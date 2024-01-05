class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def __del__(self):
        del self.stack

    def push(self, item): #thêm 1 phần tử vào stack
        if len(self.stack) < self.max_size:
            self.stack.append(item)
        else:
            print("Stack is full")

    def pop(self): #lấy 1 phần tử từ đỉnh satck
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def isEmpty(self): #kiểm tra stack có rỗng ko
        return len(self.stack) == 0

    def isFull(self): #kiểm tra stack có đầy ko
        return len(self.stack) == self.max_size

    def count(self): #đếm số phần tử trong stack
        return len(self.stack)