
from linked_list_node import LinkedListNode


class CustomQueue():
    def __init__(self):

        self.head = None
        self.tail = None
        self._count = 0

    @property
    def count(self):
        return self._count
    
    @property
    def is_empty(self):
        if self._count == 0:
            return True
        return False


    def enqueue(self, value):
        new_node = LinkedListNode(value)
        if self.is_empty == True:
            self.tail = new_node
            self.head = new_node
            self._count += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self._count += 1

    def dequeue(self):
        if not self.head:
            raise ValueError("Queue is empty")
        val = self.head.value
        self.head = self.head.next
        self._count -= 1
        return val
    
    def peek(self):
        if not self.head:
            raise ValueError("Queue is empty")
        return self.head.value
    