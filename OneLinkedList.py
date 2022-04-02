from Node import Node


class OneLinkedList:

    def __init__(self):
        self.zero = Node(None, None)
        self.len = 0

    def addStart(self, element):
        self.zero.next = Node(self.zero.next, element)
        self.len += 1

    def addEnd(self, element):
        if self.zero.next is None:
            self.zero.next = Node(None, element)
        else:
            thisNode = self.zero
            while thisNode.next is not None:
                thisNode = thisNode.next
            thisNode.next = Node(None, element)
        self.len += 1

    def add(self, element, i):
        paste = self.zero
        for a in range(i + 1):
            if paste.next is None:
                return False
            elif a == i:
                paste.next = Node(paste.next, element)
            else:
                paste = paste.next
        self.len += 1
        return True

    def getElemByIndex(self, i):
        ret = self.zero
        for a in range(i + 1):
            if ret.next is None:
                return None
            else:
                ret = ret.next
        return ret.value

    def length(self):
        return self.len
