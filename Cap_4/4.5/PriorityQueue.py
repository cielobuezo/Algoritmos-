
class PriorityQueue(object):
    def __init__(self): # Constructor
        self.head = None
 
    def insert(self, item, priority): # Insert item at rear of
        new_node = self.Node(item, priority)
        if self.head is None:
            self,head = new_node
        
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next >=priority:
                current_node = current_node.next
            if current_node.priority >= priority:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
        self.size +=1
        
    def remove(self): # Return front item of priority
        if self.head is None: # queue, if not empty, & remove
            raise Exception("Queue underflow")
        max_priority_node = self.head
        prev_node = None
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.priority > max_priority_node.priority:
                max_priority_node = current_node.next
                prev_node = current_node
            current_node = current_node.next
        if prev_node is None:
            self.head = max_priority_node.next
        else:
            prev_node.next = max_priority_node.next
        self.size -=1
        
    def peek(self): # Return frontmost 
        if self.head is None:
            return None
        return self.head.data
 
    def isEmpty(self): 
        return self.__nItems == 0
    
    def __len__(self): 
        return self._size
    
    def __str__(self): # Convert pri. queue to string
        current_node = self.head
        result = []
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next
        return "[" + ",".join(result) + "]"
