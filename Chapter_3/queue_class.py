class Sentinel:
    pass

sentinel = Sentinel()

class Queue:
    def create(self, size):
        self.array = [sentinel]*size
        self.size = size
        self.front = 0
        self.rear = 0
        self.tag = False

    def is_empty(self):
        return self.front == self.rear and not self.tag

    def is_full(self):
        return self.front == self.rear and self.tag

    def add(self, item):
        if self.is_full():
            return False
        else:
            self.rear = (self.rear+1) % self.size
            self.array[self.rear] = item
            if self.rear == self.front:
                self.tag = True
            
            return True

    def delete(self):
        if self.is_empty():
            return False
        else:
            self.front = (self.front+1) % self.size
            item = self.array[self.front]
            self.array[self.front] = sentinel
            if self.front == self.rear:
                self.tag = False
            print(item)
            return True
        

if __name__ == "__main__":
    q = Queue()
    q.create(2)
    print(f"queue is full: {q.is_full()}")
    print(f"queue is empty: {q.is_empty()}")
    print(f"queue add 10: {q.add(10)}")
    print(f"queue is full: {q.is_full()}")
    print(f"queue is empty: {q.is_empty()}")
    print(f"queue add 20: {q.add(20)}")
    print(f"queue add 30: {q.add(30)}")
    print(f"queue delete: {q.delete()}")
    print(f"queue is full: {q.is_full()}")
    print(f"queue is empty: {q.is_empty()}")