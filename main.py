from OneLinkedList import OneLinkedList

lst = OneLinkedList()


lst.addEnd(0)
lst.addEnd(1)
lst.addEnd(2)


for i in range(3):
    print(lst.getElemByIndex(i), end=" ")
print(lst.search(1))
lst.delete(2)
print()
for i in range(3):
    print(lst.getElemByIndex(i), end= " ")
