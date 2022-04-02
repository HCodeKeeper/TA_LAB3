from OneLinkedList import OneLinkedList


class LinkedStack:

    def __init__(self):
        self.elements = OneLinkedList()

    def push(self, element):
        self.elements.addStart(element)

    def pop(self):
        elem = self.elements.getElemByIndex(0)
        self.elements.delStart()
        return elem
