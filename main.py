
from LinkedStack import LinkedStack

stck = LinkedStack()

stck.push(1)
stck.push(2)
stck.push(3)
stck.push(4)

print(stck.search(4))
for i in range(5):
    print(stck.pop())


