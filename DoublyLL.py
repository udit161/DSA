class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLL:        
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        t = self.head
        while (t.next != None):
            t = t.next
        t.next = temp
        temp.prev = t

    def insertAtBeg(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAtMiddle(self, value, x):
        # element searching code
        t = self.head
        while(t != None):
            if(t.data == x):
                break
            t = t.next
            
        if t is None:
            print(f"Element {x} not found to insert after")
            return
            
        #insertion code
        temp = Node(value)
        temp.next = t.next
        temp.prev = t
        if t.next is not None:
            t.next.prev = temp
        t.next = temp        
    

    def deletetionDLL(self, value):
        if(self.head == None):
            print("Linked list is empty")
            return
            
        t = self.head
        # Traverse to find the node containing the value
        while(t != None):
            if(t.data == value):
                break
            t = t.next
            
        if(t == None):
            print("Element not found")
            return
            
        # If the node to delete is the head node
        if(t == self.head):
            self.head = t.next
            if self.head is not None:
                self.head.prev = None
            return
            
        # Re-link the adjacent nodes
        t.prev.next = t.next
        if t.next is not None:
            t.next.prev = t.prev

    def printDoublyLL(self):
        if self.head is None:
            print("List is empty")
            return
        t1 = self.head
        while(t1 != None):
            print(t1.data)
            t1 = t1.next

obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtMiddle(15,10) 
obj.deletetionDLL(20)
obj.printDoublyLL()