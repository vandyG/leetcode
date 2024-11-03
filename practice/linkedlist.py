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

