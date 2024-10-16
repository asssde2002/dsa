

class Stack:
    # def __init__(self, size):
    #     self.create(size)

    def create(self, size):
        self.array = list()
        self.size = size

    def is_full(self):
        return True if len(self.array) == self.size else False
    
    def is_empty(self):
        return True if len(self.array) == 0 else False
    
    def push(self, item):
        if self.is_full():
            return False
        else:
            self.array.append(item)
            return True
        
    def pop(self, index=-1):
        if self.is_empty():
            return False
        else:
            item = self.array.pop(index)
            return True
        
    def top(self):
        if self.is_empty():
            return None
        else:
            return self.array[-1]
        

if __name__ == "__main__":
    s = Stack()
    s.create(1)
    print(f"stack is full: {s.is_full()}")
    print(f"stack is empty: {s.is_empty()}")
    print(f"stack push 10: {s.push(10)}")
    print(f"stack is full: {s.is_full()}")
    print(f"stack is empty: {s.is_empty()}")
    print(f"stack push 20: {s.push(20)}")
    print(f"stack top: {s.top()}")
    print(f"stack pop: {s.pop()}")
