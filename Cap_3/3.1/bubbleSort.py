class BubbleSort:
    def __init__(self, a):
        self.__a = a
        self.__nItems = len(a)

    def swap(self, i, j):
        self.__a[i], self.__a[j] = self.__a[j], self.__a[i]

    def bidirectionalBubbleSort(self):
        left = 0
        right = self.__nItems - 1
        while left < right:
            # Sort from left to right
            for i in range(left, right):
                if self.__a[i] > self.__a[i+1]:
                    self.swap(i, i+1)
            right -= 1

            # Sort from right to left
            for i in range(right, left, -1):
                if self.__a[i-1] > self.__a[i]:
                    self.swap(i-1, i)
            left += 1

# Ejemplo de prueba
a = [5, 3, 8, 4, 2]
bs = BubbleSort(a)
bs.bidirectionalBubbleSort()
assert bs._BubbleSort__a == [2, 3, 4, 5, 8] # Verifica si la lista ha sido ordenada correctamente
