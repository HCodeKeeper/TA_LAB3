from LinkedStack import LinkedStack

stck = LinkedStack()

stck.push(1)    # 1st elem now
stck.push(2)    # 1st elem now
stck.push(3)    # 1st elem now

print(stck.search(3))   # 0th index
print(stck.pop())       # remove 3 from stack
print(stck.search(3))   # there is no 3 (index -1)
print(stck.search(2))   # 2 is first element now
print(stck.pop())
print(stck.pop())       # stack is empty now
print(stck.search(1))



