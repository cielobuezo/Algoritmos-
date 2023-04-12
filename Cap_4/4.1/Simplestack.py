# Implement a Stack data structure using a Python list

class Stack(object):
    def __init__(self, max_size): # Constructor
        self.max_size = max_size # Maximun size of stack
        self.stack_list = [None] * max_size # The stack stored as a list
        self.top = -1 # No items initially
       
        
    def push(self, item): # Insert item at top of stack
        if self.is_full():
            raise Exception("Stack is full")
        self.top += 1 # Advance the pointer
        self.stack_list[self.top] = item # Store item
 
    def pop(self): # Remove top item from stack
        if self.is_empty():
            raise Exception("Stack is empty")
        item = self.stack_list[self.top] # Top item
        self.stack_list[self.top] = None # Remove item reference
        self.top -= 1 # Decrease the pointer
        return item # Return top item
 
    def peek(self): # Return top item
        if not self.is_empty(): # If stack is not empty
            return self.stack_list[self.top] # Return the top item
 
    def is_empty(self): # Check if stack is empty
        return self.top == -1
 
    def is_full(self): # Check if stack is full
        return self.top == self.max_size - 1
 
    def __len__(self): # Return # of items on stack
        return self.top + 1
 
    def __str__(self): # Convert stack to string
        if self.is_empty():
            return "[]"
        else:
            s = "["
            for i in range(self.top):
                s += str(self.stack_list[i]) + ","
            s += str(self.stack_list[self.top]) + "]"
            return s
                
