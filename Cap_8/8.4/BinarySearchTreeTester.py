# Test the BinarySearchTree class interactively
from BinarySearchTree import *
bst = BinarySearchTree()

keys_list = [   [7, 6, 5, 4, 3, 2, 1, 8, 12, 10, 9, 11, 14, 13, 15],
                [8, 4, 5, 6, 7, 3, 2, 1, 12, 10, 9, 11, 14, 13, 15],
                [8, 4, 2, 3, 1, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15],
                [8, 4, 2, 3, 1, 6, 5, 7, 12, 10, 9, 11, 14, 13, 8, 5]
            ]

for keys in keys_list:
    for key in keys:
        bst.insert(key)

print("Árbol resultante:")
bst.inorder_traversal()

print("Balance de nivel del nodo raíz:")
print(bst.levelBalance())

print("Llaves no balanceadas con by=1:")
print(bst.unbalancedNodes(by=1))

print("Llaves no balanceadas con by=2:")
print(bst.unbalancedNodes(by=2))
