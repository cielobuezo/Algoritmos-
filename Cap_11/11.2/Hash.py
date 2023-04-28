class HashTable:
    """
    Una tabla hash con sondeo lineal y conteo de llaves desplazado.
    """
    def __init__(self, size, hash_func):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.hash_func = hash_func

    def __getitem__(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        raise KeyError(f"Key '{key}' not found.")

    def __setitem__(self, key, value):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def __delitem__(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self._rehash(index)
                return
            index = (index + 1) % self.size
        raise KeyError(f"Key '{key}' not found.")

    def _rehash(self, index):
        """
        Rehash las entradas después de eliminar un elemento.
        """
        current = index
        next = (index + 1) % self.size
        while self.keys[next] is not None:
            hash_next = self.hash(self.keys[next])
            if (next < hash_next <= current) or (current < next < hash_next) or (hash_next <= current < next):
                self.keys[current] = self.keys[next]
                self.values[current] = self.values[next]
                self.keys[next] = None
                self.values[next] = None
                current = next
            next = (next + 1) % self.size

    def hash(self, key):
        """
        Calcula el índice de hash para una clave dada.
        """
        return self.hash_func(key, self.size)
    
def hash_func_1(key, size):
    key_str = str(key)
    result = 0
    # Itera a través de la cadena de clave en pasos de 3 caracteres
    for i in range(0, len(key_str), 3):
        # Obtén el grupo de tres caracteres actual
        group = key_str[i:i+3]
        # Agrega el valor del grupo actual al resultado
        result += int(group)
    # Calcula el índice de hash tomando el resto del resultado dividido por el tamaño de la tabla hash
    return result % size


    
   
def hash_func_2(key, size):
    key_str = str(key)
    result = 0
    for i in range(0, len(key_str), 2):
        group = key_str[i:i+2]
        result += int(group)
    return result % size

table1 = HashTable(size=100, hash_func=hash_func_1)
table2 = HashTable(size=100, hash_func=hash_func_2)

table1['foo']= 'bar'
table2[42] = 'baz'

del table1['foo']
