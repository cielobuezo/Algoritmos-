class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(matrix):
    root = Node(matrix[0][0])
    nodes = {(0, 0): root}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] is not None:
                if (i, j) not in nodes:
                    raise Exception("Tree construction failed: missing parent node")
                node = nodes[(i, j)]
                if i + 1 < len(matrix) and matrix[i+1][j] is not None:
                    if (i+1, j) in nodes:
                        raise Exception("Tree construction failed: duplicate node")
                    node.left = Node(matrix[i+1][j])
                    nodes[(i+1, j)] = node.left
                if j + 1 < len(matrix[i]) and matrix[i][j+1] is not None:
                    if (i, j+1) in nodes:
                        raise Exception("Tree construction failed: duplicate node")
                    node.right = Node(matrix[i][j+1])
                    nodes[(i, j+1)] = node.right
    return root

def print_tree(node):
    if node is not None:
        print(node.val)
        print_tree(node.left)
        print_tree(node.right)

# Matriz []
root = build_tree([])
print_tree(root)  # Salida: (nada)

# Matriz [n, n, n]
root = build_tree([[None, None, None]])
print_tree(root)  # Salida: n, n, n

# Matriz [55, 12, 71]
root = build_tree([[55, 12, 71]])
print_tree(root)  # Salida: 55, 12, 71

# Matriz [55, 12, n, 4]
root = build_tree([[55, 12, None, 4]])
print_tree(root)  # Salida: 55, 12, 4

# Matriz [55, 12, n, 4, n, n, n, n, 8, n, n, n, n, n, n, n, n, 6, n]
root = build_tree([[55, 12, None, 4, None, None, None, None, 8, None, None, None, None, None, None, None, None, 6, None]])
print_tree(root)  # Salida: 55, 12, 4, 8, 6

# Matriz [55, 12, n, n, n, n, 4, n, 8, n, n, n, n, n, n, n, n, 6, n]
root = build_tree([[55, 12, None, None, None, None, 4, None, 8, None, None, None, None, None, None, None, None, 6, None]])
print_tree(root)  # Salida: 55, 12, 4, 8, 6

