class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLinkedList:

    def __init__(self,head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp      

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next    

obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.printLL() 
