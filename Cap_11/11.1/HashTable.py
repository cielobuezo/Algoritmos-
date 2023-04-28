import random

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        
    def hash(self, key):
        # Implementar la función hash
        return hash(key) % self.capacity
    
    def linear_probe(self, index, i):
        return (index + i) % self.capacity
    
    def quadratic_probe(self, index, i):
        return (index + i**2) % self.capacity
    
    def double_hash(self, key, i):
        return (self.hash(key) + i * (1 + (hash(key) % (self.capacity - 1)))) % self.capacity
    
    def put(self, key, value, probe):
        index = self.hash(key)
        i = 0
        while self.table[index] is not None:
            i += 1
            index = probe(index, i)
        self.table[index] = (key, value)
        
    def get(self, key, probe):
        index = self.hash(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
            index = probe(index, i)
        return None
    
    def getCollisions(self):
        collisions = []
        for index in range(self.capacity):
            if self.table[index] is not None and len(self.table[index]) > 1:
                collisions.append(self.table[index][0])
        return collisions
    
    def getDisplacementCounts(self, probe, load_factor):
        self.table = [None] * self.capacity
        num_insertions = int(load_factor * self.capacity)
        keys = [random.randint(0, 1000000) for i in range(num_insertions)]
        values = [random.random() for i in range(num_insertions)]
        for i in range(num_insertions):
            self.put(keys[i], values[i], probe)
        displacements = []
        for i in range(num_insertions):
            key = keys[i]
            index = self.hash(key)
            j = 0
            while self.table[index] is not None and self.table[index][0] != key:
                j += 1
                index = probe(index, j)
            if self.table[index] is None:
                displacements.append(None)
            else:
                displacements.append(j)
        return displacements
    
table = HashTable(103)
keys = random.sample(range(1000), 200)
values = [random.random() for i in range(200)]
for i in range(200):
    table.put(keys[i], values[i], table.linear_probe)
displacements = table.getDisplacementCounts(table.linear_probe, 0.5)
collisions = table.getCollisions()
print("Displacements:", displacements)
print("Collisions:", collisions)
