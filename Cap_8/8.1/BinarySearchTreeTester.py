from BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()

# insertar claves duplicadas
bst.insert(10)
bst.insert(20)
bst.insert(30)
bst.insert(10)
bst.insert(20)
bst.insert(30)

# imprimir la cuenta de cada clave
print(bst.buscar(10).cuenta) # debería imprimir 2
print(bst.buscar(20).cuenta) # debería imprimir 2
print(bst.buscar(30).cuenta) # debería imprimir 2

# eliminar claves duplicadas
bst.eliminar(30)
bst.eliminar(20)
bst.eliminar(10)

# imprimir la cuenta de cada clave
print(bst.buscar(10).cuenta) # debería imprimir 1
print(bst.buscar(20).cuenta) # debería imprimir 1
print(bst.buscar(30)) # debería imprimir None
