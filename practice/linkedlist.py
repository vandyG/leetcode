class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self, node=None):
        if not node:
            node = self.head
        while node:
            print(node.val)
            node = node.next
    
    def search(self, val):
        node = self.head
        while node:
            if node.val == val:
                return True
            node = node.next
        return False
    
    @property
    def length(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def prepend(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
    
    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
    
    def insert(self, value, index):
        
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(value)
            return
        
        node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        node.next = current.next
        current.next = node

    def delete(self, index):
        node = self.head
        pass