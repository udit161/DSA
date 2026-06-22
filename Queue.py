class Queue:
    def __init__(self):
        self.items = []


    def isEmpty(self):
        return len(self.items) == 0

    def insert(self, value):
        self.items.append(value)

    def delete(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        self.items.pop(0)
        
    def peek(self):
        return self.items[0]
        
    def display(self):
        for i in self.items:
            print(i)

obj = Queue()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.display()
print("-" * 10)
obj.delete()
obj.display()            