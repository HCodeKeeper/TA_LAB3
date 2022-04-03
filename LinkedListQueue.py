from LinkedList import MyLinkedList


class LinkedListQueue:

    def __init__(self):
        self.queue = MyLinkedList()

    def put(self, data):
        self.queue.append(data)

    def remove(self):
        self.queue.delete_start()

    def element(self):
        return self.queue.head.data

