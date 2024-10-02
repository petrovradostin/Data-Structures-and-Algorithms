from linked_list_node import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self._head: LinkedListNode = None
        self._tail: LinkedListNode = None
        self._count = 0

    @property
    def count(self):
        return self._count

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def add_first(self, value):
        new_node = LinkedListNode(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._count += 1

    def add_last(self, value):
        new_node = LinkedListNode(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._count += 1

    def insert_after(self, node: LinkedListNode, value):
        new_node = LinkedListNode(value)
        if node is None:
            raise ValueError("The node is None")
        
        if node == self._tail:
            new_node.next = None
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        else:
            new_node.next = node.next
            new_node.prev = node
            node.next.prev = new_node
            node.next = new_node
        self._count += 1

    def insert_before(self, node: LinkedListNode, value):
        new_node = LinkedListNode(value)
        if node is None:
            raise ValueError("The node is None")
        
        if node == self._head:
            new_node.next = self._head
            new_node.prev = None
            self._head.prev = new_node
            self._head = new_node
        else:
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
        self._count += 1
            
    def remove_first(self):
        if self._head is None:
            raise ValueError("The list is empty")  
        value = self._head.value
        self._head = self._head.next
        self._count -= 1
        return value

    def remove_last(self):
        if self._head is None:
            raise ValueError("The list is empty")
        value = self._tail.value
        self._tail = self._tail.prev
        self._count -= 1
        return value

    def find(self, value):
        current = self._head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def values(self):
        values_list = []
        current = self._head
        while current is not None:
            values_list.append(current.value)
            current = current.next
        return tuple(values_list)

    def _insert_before_head(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self._head
        new_node.prev = None
        new_node = self._head

    def _insert_after_tail(self, value):
        new_node = LinkedListNode(value)
        new_node.next = None
        new_node.prev = self._tail
        new_node = self._tail
