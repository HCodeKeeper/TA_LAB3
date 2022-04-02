class Node:
    def __init__(self, nxt, value):
        self.next = nxt
        self.value = value


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

    def delStart(self):
        if self.zero.next is None:
            return False
        self.zero.next = self.zero.next.next
        self.len -= 1
        return True

    def delEnd(self):
        if self.zero.next is None:
            return False
        if self.zero.next.next is None:
            self.zero.next = None
            return True
        thisNode = self.zero.next
        while thisNode.next.next is not None:
            thisNode = thisNode.next
        thisNode.next = None
        return True

    def delete(self, i):
        if self.zero.next is None:
            return False
        thisNode = self.zero
        for a in range(0, i + 1):
            if thisNode.next is None:
                return False
            elif a == i:
                thisNode.next = thisNode.next.next
            else:
                thisNode = thisNode.next
        self.len -= 1
        return True

    def length(self):
        return self.len
