from LinkedList import MyLinkedList


class LinkedStack:

    def __init__(self):
        self.elements = MyLinkedList()

    def push(self, element):
        self.elements.prepend(element)

    def pop(self):
        elem = self.elements.head.data
        self.elements.delete_start()
        return elem

    def search(self, element):
        return self.elements.get_element_index(element)
