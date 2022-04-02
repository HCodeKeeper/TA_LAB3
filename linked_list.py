from argparse import ArgumentError

class Node:
    def __init__(self, curr, prev=None, next=None):
        self.prev = prev
        self.curr = curr
        self.next = next
    
    def __str__(self):
        return str(self.curr)
    
    
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0   
    
    def __link_first(self, val):
        if val == None:
            raise ArgumentError(None, message="Can't add None value to doubly linked list")

        if self.head == None:
            self.head = Node(val)
        else:
            node = Node(val, next=self.head)
            self.head.prev = node
            self.head = node
    
    def __link_last(self, val):
        if val == None:
            raise ArgumentError(None, message="Can't add None value to doubly linked list")

        if self.head == None:
            self.__link_first(val)
        elif self.tail == None:
            self.tail = Node(val, prev=self.head)
            if self.head.next == None:
                self.head.next = self.tail
        else:
            node = Node(val, prev=self.tail)
            self.tail.next = node
            self.tail = node
    
    def add(self, val):
        if val == None:
            raise ArgumentError(None, message="Can't add None value to doubly linked list")
        self.__link_last(val)
        self.size += 1
    
    def push(self, val):
        if val == None:
            raise ArgumentError(None, message="Can't add None value to doubly linked list")
        self.__link_first(val)
        self.size += 1 
    
    def insert(self, ind, val):
        prev_node = self.__get_at(ind)
        next_node = prev_node.next
        node = Node(val, prev_node, next_node)
        prev_node.next = node
        if next_node != None:
            next_node.prev = node
        self.size += 1

    def is_empty(self):
        return self.head == None
    
    def pop(self):
        if self.is_empty():
            raise ArgumentError(None, message="The list is empty")
        elif self.tail == None:
            self.head = None
        else:
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail = prev_node
        self.size -= 1
    
    def delete_first(self):
        if self.head == None:
            raise ArgumentError(None, "The list is empty")
        if self.head.next == None: # можно допилить на проверку класса
            self.head = None
        elif self.head.next == self.tail:
            self.tail.prev = None
            self.head = self.tail
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        self.size -= 1
    
    def delete_at(self, ind):
        if ind == 0:
            self.delete_first()
        elif ind == self.size - 1:
            self.pop()
        else:
            node = self.__get_at(ind)
            prev_node = node.prev
            prev_node.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        

    def get_first(self):
        return self.head.curr
    
    def get_last(self):
        return self.tail.curr

    def get_generator(self):
        node = Node(None, next=self.head)
        while node.next != None:
            node = node.next
            yield node

    def __get_at(self, ind):
        if ind >= self.size or ind < 0:
            raise ArgumentError(None, message="There is no element with such index. It's likely the index is out of size bounds")     
        else:
            if ind <= self.size // 2:
                node = self.head
                for i in range(ind+1):
                    if i != 0:
                        node = node.next
                return node
            else:
                node = self.tail
                for i in range(self.size-1, ind-1, -1):
                    if i != self.size-1:
                        node = node.prev
                return node
    
    def get_at(self, ind):
        return self.__get_at(ind).curr
    
    def get_by_value(self, value):
        index = -1
        for node in self.get_generator():
            index += 1
            if node.curr == value:
                return index
        raise ArgumentError(None, message="This value doesn't exist in the linked list")
