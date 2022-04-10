class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value


class CircularLinkedList:

    def __init__(self):
        self.head = Node(None, None)
        self.length = 0

    def add_start(self, element):
        if self.head.value is None:
            self.head.value = element
        if self.head.next is None:
            self.head.next = self.head
        else:
            self.head.next = Node(self.head.next, self.head.value)
            self.head.value = element
            self.length += 1
        return

    def add_end(self, element):
        if self.head.value is None:
            self.head.value = element
        if self.head.next is None:
            self.head.next = self.head
        change = self.head
        while change.next != self.head:
            change = change.next
        change.next = Node(self.head, element)
        self.length += 1
        return

    def add_id(self, element, add_id):
        self.length += 1
        change = self.head
        if add_id==0:
            self.add_start(element)
            return
        if add_id==self.length+1:
            self.add_end(element)
            return
        for i in range(add_id):
            if i == add_id-1:
                change.next = Node(change.next, element)
                break
            else:
                change = change.next
        return

    def del_start(self):
        change=self.head
        while change.next != self.head:
            change = change.next
        change.next=Node(self.head.next.next,self.head.next.value)
        self.head = None
        self.head=change.next
        self.length -= 1
        return

    def del_end(self):
        change=self.head
        for i in range(self.length-2):
            change=change.next
        change.next = Node(change.next.next.next, change.next.value)
        self.length -= 1
        return

    def del_id(self, delete_id):
        change = self.head
        if delete_id==0:
            self.del_start()
            return
        if delete_id==self.length+1:
            self.del_end()
            return
        if delete_id==1:
            self.head.next = Node(change.next.next.next, change.next.next.value)
            self.length -= 1
            return
        for i in range(delete_id-2):
            change = change.next
        change.next = Node(change.next.next.next, change.next.value)
        self.length -= 1
        return

    def search_element(self, search_id):
        index = 0
        change = self.head
        while index < self.length:
            if change.value == search_id:
                return index
            else:
                index += 1
                change = change.next
        return index

    def get_length(self):
        return self.length
