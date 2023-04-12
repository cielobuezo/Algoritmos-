class BinaryTree:
    def __init__(self, value=None):
        if value is not None:
            self.root = Node(value)
        else:
            self.root = None

    def is_empty(self):
        return self.root is None

    def combine(self, operator, other_tree):
        new_tree = BinaryTree()
        new_tree.root = Node(operator)
        new_tree.root.left = self.root
        new_tree.root.right = other_tree.root
        return new_tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_expression_tree(s):
    stack = []
    for c in s:
        if c.isdigit():
            node = Node(int(c))
            stack.append(node)
        else:
            right = stack.pop()
            left = stack.pop()
            node = Node(c)
            node.left = left
            node.right = right
            stack.append(node)
    return stack.pop()

def nextToken(s):
    for c in s:
        if c.isdigit():
            yield int(c)
        elif c in "+-*/":
            yield c

def construct_expression_tree(s):
    stack = []
    for c in s:
        if c.isdigit():
            node = Node(int(c))
            stack.append(node)
        else:
            right = stack.pop()
            left = stack.pop()
            node = Node(c)
            node.left = left
            node.right = right
            stack.append(node)

    if len(stack) != 1:
        raise ValueError("La expresión de entrada no produce una sola expresión algebraica")

    return stack.pop()

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def preorder_traversal(self):
        """
        Realiza un recorrido preorden del árbol binario
        """
        traversal = []
        traversal.append(str(self.value))
        if self.left is not None:
            traversal += self.left.preorder_traversal()
        if self.right is not None:
            traversal += self.right.preorder_traversal()
        return traversal

    def inorder_traversal(self):
        """
        Realiza un recorrido en orden del árbol binario
        """
        traversal = []
        if self.left is not None:
            traversal += self.left.inorder_traversal()
        traversal.append(str(self.value))
        if self.right is not None:
            traversal += self.right.inorder_traversal()
        return traversal

    def postorder_traversal(self):
        """
        Realiza un recorrido en postorden del árbol binario
        """
        traversal = []
        if self.left is not None:
            traversal += self.left.postorder_traversal()
        if self.right is not None:
            traversal += self.right.postorder_traversal()
        traversal.append(str(self.value))
        return traversal

# Creamos el árbol para la expresión a
exp_a = construct_expression_tree('9195+15+19+4*')
print('Expresión a:')
print('Recorrido preorden:', exp_a.root.preorder_traversal())
print('Recorrido en orden:', exp_a.root.inorder_traversal())
print('Recorrido en postorden:', exp_a.root.postorder_traversal())

# Creamos el árbol para la expresión b
exp_b = construct_expression_tree('BB*AC4**-')
print('Expresión b:')
print('Recorrido preorden:', exp_b.root.preorder_traversal())
print('Recorrido en orden:', exp_b.root.inorder_traversal())
print('Recorrido en postorden:', exp_b.root.postorder_traversal())

# Creamos el árbol para la expresión c
exp_c = construct_expression_tree('42')
print('Expresión c:')
print('Recorrido preorden:', exp_c.root.preorder_traversal())
print('Recorrido en orden:', exp_c.root.inorder_traversal())
print('Recorrido en postorden:', exp_c.root.postorder_traversal())

# Creamos el árbol para la expresión d
exp_d = construct_expression_tree('A57')
print('Expresión d:')
print('Recorrido preorden:', exp_d.root.preorder_traversal())
print('Recorrido en orden:', exp_d.root.inorder_traversal())
print('Recorrido en postorden:', exp_d.root.postorder_traversal())
           

