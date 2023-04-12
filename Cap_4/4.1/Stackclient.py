from SimpleStack import Stack

stack = Stack(3)

print("Stack:", stack)

stack.push(1)
print("Stack:", stack)

stack.push(2)
print("Stack:", stack)

stack.push(3)
print("Stack:", stack)

try:
    stack.push(4)
except Exception as e:
    print(e) #expect exception "stack is full"
    
item = stack.pop()
print("Popped item:", item)
print("Stack:", stack)

item = stack.pop()
print("Popped item:", item)
print("Popped:", stack)

item = stack.pop
print("Popped item:", item)
print("Popped:", stack)

try:
    item = stack.pop()
except Exception as e:
    print(e)
