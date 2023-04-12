class Array(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if 0 <= n < self.__nItems:
            return self.__a[n]

    def set(self, n, value):
        if 0 <= n < self.__nItems:
            self.__a[n] = value

    def swap(self, j, k):
        if 0 <= j < self.__nItems and 0 <= k < self.__nItems:
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):
        if self.__nItems >= len(self.__a):
            raise Exception("Array overflow")
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        raise ValueError("Item not found")

    def search(self, item):
        try:
            return self.get(self.find(item))
        except ValueError:
            return None

    def delete(self, item):
        try:
            j = self.find(item)
        except ValueError:
            return False
        self.__nItems -= 1
        for k in range(j, self.__nItems):
            self.__a[k] = self.__a[k + 1]
        return True

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans += "]"
        return ans

    def median(self):
        if self.__nItems == 0:
            return None

        self.bubbleSort()

        mid = self.__nItems // 2

        if self.__nItems % 2 == 0:
            return (self.__a[mid - 1] + self.__a[mid]) / 2.0
        else:
            return self.__a[mid]

    def bubbleSort(self):
        for last in range(self.__nItems - 1, 0, -1):
            for inner in range(last):
                if self.__a[inner] > self.__a[inner + 1]:
                    self.swap(inner, inner + 1)

    def selectionSort(self):
        for outer in range(self.__nItems - 1):
            min = outer
            for inner in range(outer + 1, self.__nItems):
                if self.__a[inner] < self.__a[min]:
                    min = inner
            self.swap(outer, min)

    def insertionSort(self):
        for outer in range(1, self.__nItems):
            temp = self.__a[outer]
            inner = outer
            while inner > 0 and temp < self.__a[inner - 1]:
                self.__a[inner] = self.__a[inner - 1]
                inner -= 1
            self.__a[inner] = temp
        
my_array = Array(10) # create an array of size 10
my_array.insert(5) # insert some elements into the array
my_array.insert(3)
my_array.insert(8)
my_array.insert(1)
my_array.insert(9)

print("Original array:", my_array) # print the original array

my_array.bubbleSort() # sort the array using bubble sort
print("Sorted array using bubble sort:", my_array)

my_array.selectionSort() # sort the array using selection sort
print("Sorted array using selection sort:", my_array)

my_array.insertionSort() # sort the array using insertion sort
print("Sorted array using insertion sort:", my_array)

print("Median of the array:", my_array.median()) # calculate the median of the array
