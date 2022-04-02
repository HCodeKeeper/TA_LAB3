from OneLinkedList import OneLinkedList

lst = OneLinkedList()


lst.addEnd(0)
lst.addStart(1)
lst.addStart(2)
lst.addStart(4)
lst.add(5, 2)

for i in range(5):
    print(lst.getElemByIndex(i))
