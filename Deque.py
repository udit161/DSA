class Deque:
    def __init__(self):
        self.items = []


    def isEmpty(self):
        return len(self.items) == 0

    def insertAtLast(self, value):
        self.items.append(value)

    def deleteAtFront(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        self.items.pop(0)


    def deleteAtLast(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        self.items.pop()

    def insertAtFront(self, value):
        self.items.insert(0, value)
    
    def peekAtFront(self):
        return self.items[0]
        
    def peekAtLast(self):
        return self.items[-1]
    
    def display(self):
        for i in self.items:
            print(i)

obj = Deque()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.display()
print("-" * 10)
obj.delete()
obj.display()               