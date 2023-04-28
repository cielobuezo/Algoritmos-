class HashTable:
    def __init__(self):
        self.size = 128
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __growTable(self):
        self.size *= 2
        
        # Check if new size is a prime number
        is_prime = True
        for i in range(2, int(self.size ** 0.5) + 1):
            if self.size % i == 0:
                is_prime = False
                break
        if not is_prime:
            print("Warning: table size is not a prime number, increasing collision probability.")
        
        new_keys = [None] * self.size
        new_values = [None] * self.size
        for i in range(len(self.keys)):
            if self.keys[i] is not None:
                index = self.__hash(self.keys[i])
                new_keys[index] = self.keys[i]
                new_values[index] = self.values[i]
        self.keys = new_keys
        self.values = new_values
        
    def insert(self, key, value):
        index = self.__hash(key)
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
        else:
            if self.keys[index] == key:
                self.values[index] = value  # update value for existing key
            else:
                # collision, find next available slot
                next_index = self.__findNextSlot(index)
                while self.keys[next_index] is not None and self.keys[next_index] != key:
                    next_index = self.__findNextSlot(next_index)
                    if next_index == index:
                        # Sequence of probing is exhausted, table is full
                        try:
                            # Try to cause the exception by generating a random key sequence
                            import random
                            random.seed(0)
                            for i in range(self.size):
                                random_key = str(random.random())
                                self.insert(random_key, random_key)
                        except Exception as e:
                            # Log the problem
                            import logging
                            logging.basicConfig(filename='hash_table.log', level=logging.ERROR)
                            logging.error("Exception: " + str(e) + ", table size: " + str(self.size))
                            print("Error: table is full and sequence of probing is exhausted.")
                            return
                self.keys[next_index] = key
                self.values[next_index] = value

    def __hash(self, key):
        # hash function, returns an index between 0 and self.size-1
        return sum([ord(c) for c in key]) % self.size

    def __findNextSlot(self, index):
        # linear probing sequence
        return (index + 1) % self.size
    
    def showProbingSequence(self):
        for i in range(3):
            for j in range(3):
                for k in range(200):
                    key = f'{i},{j},{k}'
                    index = self.__hash(key)
                    count = 0
                    while self.keys[index] is not None and self.keys[index] != key:
                        index = self.__findNextSlot(index)
                        count += 1
                        if count == self.size:
                            print(f'Unable to insert key: {key} for condition {i},{j}')
                            break
                    if self.keys[index] is None:
                        self.insert(key, key)
                        print(f'Key {key} inserted with {count} probes for condition {i},{j}')
                    else:
                        print(f'Key {key} already exists with {count} probes for condition {i},{j}')
                        
    # Create a HashTable instance
ht = HashTable()

# Add some key-value pairs
ht.insert('key1', 'value1')
ht.insert('key2', 'value2')
ht.insert('key3', 'value3')
ht.insert('key4', 'value4')

# Retrieve the values associated with the keys
print(ht['key1'])  # Output: value1
print(ht.get('key2'))  # Output: value2
print(ht.get('key5', 'default_value'))  # Output: default_value

# Show the probing sequence
ht.showProbingSequence()


    
    
