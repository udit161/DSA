"""Module containing classes to represent and manipulate a Singly Linked List."""


class Node:
    """A class representing a single node in a linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node with data and an optional reference to the next node."""
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    """A class representing a Singly Linked List."""

    def __init__(self, head=None):
        """Initialize the singly linked list with an optional head node."""
        self.head = head

    def insert_at_end(self, value):
        """Insert a new node with the given value at the end of the list."""
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def print_ll(self):
        """Print the values of the nodes in the list sequentially."""
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


# Demonstration
obj = SinglyLinkedList()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.print_ll()
