class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items =[None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        
    def insertLeft(self, item):
        if self.isFull():
            raise Exception('Deque is Full')
        self.front = (self.front - 1)%self.capacity
        self.items[self.front] = item
        self.size += 1
        
    def insertRight(self, item):
        if self.isFull():
            raise Exception('Deque is Full')
        self.items[self.rear] = item
        self.rear = (self.rear + 1)%self.capacity
        self.size += 1
    
    def removeLeft(self):
        if self.empty():
            raise Exception('Deque is Empty')
        item  = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size  -= 1 
        return item
    
    def removeRight(self):
        if self.isEmpty(): 
            raise Exception('Deque is Empty')
        self.rear = (self.rear -1) % self.capacity
        item = self.items[self.rear]
        self.items[self.rear] = None
        self.size -= 1
        return item
    
    def peekLeft(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.items[self.front]
    
    def peekRight(self):
        if self.isEmpty():
            raise Exception('Deque is Empty')
        return self.items[(self.rear - 1)% self.capacity]
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    
