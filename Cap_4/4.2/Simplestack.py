class Stack:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def isFull(self):
        return len(self.items) == self.capacity
    
    def push(self, item):
        if not self.isFull():
            self.items.append(item)
        else:
            print("Stack is full.")
        
    def pop(self):
        if  not self.isEmpty():
            return self.items.pop()
        else:
            print ("Stack is Empty.")
    
    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            print("Stack is empty.")
    
    def size(self):
        return len(self.items)
    
def isPalindromo(word):
    stack = Stack(len(word))
    word = word.lower()
    for letter in word:
        if letter.isalnum():
            stack.push(letter)
            
    reverse=''
    while not stack.isEmpty():
        reverse += stack.pop()
        
    return word == reverse

input_str = "Un hombre, un plan un canal, Panama"
input_str = input_str.replace(" ","")
input_str = ''.join(filter(str.isalnum, input_str))

if isPalindromo(input_str):
    print(f"{input_str} es un palindromo!")
else:
    print(f"{input_str} no es un  palindromo")
    
    
