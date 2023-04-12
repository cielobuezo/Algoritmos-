class Array(object):
    def __init__(self, initialSize): # Constructor
        self.__a = [None] * initialSize # The array stored as a list
        
        self.__nItems = 0 # No items in array initially
 
    def __len__(self): # Special def for len() func
 
        return self.__nItems # Return number of items
 
    def get(self, n): # Return the value at index n
        
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
 
            return self.__a[n] # only return item if in bounds
 
    def set(self, n, value): # Set the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
 
            self.__a[n] = value # only set item if in bounds
 
    def insert(self, item): # Insert item at end
        self.__a[self.__nItems] = item # Item goes at current end
        self.__nItems += 1 # Increment number of items
 
    def find(self, item): # Find index for item
        for j in range(self.__nItems): # Among current items
            if self.__a[j] == item: # If found,
                return j # then return index to item
        return -1 # Not found -> return -1
    
    def search(self, item): # Search for item
        return self.get(self.find(item)) # and return item if found
 
    def delete(self, item): # Delete first occurrence
        for j in range(self.__nItems): # of   an item
            if self.__a[j] == item: # Found item
                self.__nItems -= 1 # One fewer at end
                for k in range(j, self.__nItems): # Move items from
                    self.__a[k] = self.__a[k+1] # right over 1
                return True # Return success flag
 
        return False # Made it here, so couldn't find the item
 
    def traverse(self, function=print): # Traverse all items
        for j in range(self.__nItems): # and apply a function
            function(self.__a[j])

#Excercise 2.1
    def getMaxNum(self):
        max = None
        for j in range (self.__nItems):
            if type(self.__a[j]) == int or type (self.__a[j]) == float:
                if max is None or self.__a[j] > max:
                    max = self.__a[j]
        return max
    
#Excercise 2.2               
    def deleteMaxNum(self):
        max = self.getMaxNum()
        if max is not None:
            self.delete(max)
            return True
        else:
            return False
        
#Exercise 2.4
    def removeDupes(self):
        unique_items = []
        for item in self.__a:
            if item not in unique_items:
                unique_items.append(item)
        self.__a = unique_items
        self.__nItems = len(unique_items)
    
                

        
    

    
    
   
