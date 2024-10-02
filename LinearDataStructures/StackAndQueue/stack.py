
from linked_list_node import LinkedListNode


class CustomStack:
    def __init__(self):
        self.top = None
        self._count = 0

    @property
    def count(self):
        return self._count
    
    @property
    def is_empty(self):
        if self._count == 0:
            return True
        return False

    def push(self, value):
        node = LinkedListNode(value)
        node.next = self.top
        self.top = node
        self._count += 1
   
    def pop(self):
        if not self.top:
            raise ValueError("Stack is empty")
        val = self.top.value
        self.top = self.top.next
        self._count -= 1
        return val
    
    def peek(self):
        if not self.top:
            raise ValueError("Stack is empty")
        return self.top.value