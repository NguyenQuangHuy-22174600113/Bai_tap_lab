class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, data):
        if len(self.stack) == self.max_size:
            print("Stack is full")
        else:
            self.stack.append(data) 

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.stack.pop()

    def is_empty(self): #kiểm tra stack có rỗng ko
        return len(self.stack) == 0

    def is_full(self): #kiểm tra stack có đầy ko
        return len(self.stack) == self.max_size

s = Stack(2)
print(s.is_empty())
s.push(1.1)  
s.push(2.2)  
print(s.is_full())
print(s.pop())