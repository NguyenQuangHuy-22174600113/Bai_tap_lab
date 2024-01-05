class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def __del__(self):
        del self.stack

    def push(self, item):
        if not self.isFull():
            self.stack.append(item)
        else:
            print("Stack is full!")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is empty!")

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.max_size

    def print(self):
        for i in reversed(self.stack):
            print(i)
