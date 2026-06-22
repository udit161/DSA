class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1

    def insert(self, value):
        if((self.rear+1)%(self.size))==self.front:
            print("Queue is full")
        elif(self.front == -1 and self.rear == -1):
            self.front = self.rear = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear+1) % (self.size)
            self.items[self.rear]  = value
    
    def deletion(self):
        if(self.front == -1 and self.rear == -1):
            print("queue is empty")
        elif(self.front == self.rear):
            self.front= self.rear = -1
        else:
            self.front=(self.front+1) % self.size
            print("Element deleted")



cq = CircularQueue(5)
cq.insert(10)
cq.insert(20)
cq.insert(30)
cq.insert(40)
cq.insert(50)
print(cq.items)
cq.deletion()
print(cq.items)