class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._insert(value, current_node.left_child)
        else:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)

    def _find(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left_child is not None:
            return self._find(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child is not None:
            return self._find(value, current_node.right_child)

    def delete(self, value):
        return self._delete(self.root, value)

    def _delete(self, current_node, value):
        if current_node is None:
            return current_node
    
        if value < current_node.value:
            current_node.left_child = self._delete(current_node.left_child, value)
        elif value > current_node.value:
            current_node.right_child = self._delete(current_node.right_child, value)
        else:
            if current_node.left_child is None:
                temp = current_node.right_child
                current_node = None
                return temp
            elif current_node.right_child is None:
                temp = current_node.left_child
                current_node = None
                return temp
            temp = self._min_value_node(current_node.right_child)
            current_node.value = temp.value
            current_node.right_child = self._delete(current_node.right_child, temp.value)
    
        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left_child is not None:
            current = current.left_child
        return current

    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)

    def _inorder_traversal(self, current_node):
        if current_node is not None:
            self._inorder_traversal(current_node.left_child)
            print(current_node.value)
            self._inorder_traversal(current_node.right_child)

    def nodeBalance(self, node):
        if node is None:
            return 0
        else:
            return self.count_nodes(node.right_child) - self.count_nodes(node.left_child)

    def count_nodes(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes(node.left_child) + self.count_nodes(node.right_child)

    def levelBalance(self):
        if self.root is None:
            return 0
        else:
            right_levels = self.count_levels(self.root.right_child)
            left_levels = self.count_levels(self.root.left_child)
            return right_levels - left_levels


    def count_levels(self, node):
        if node is None:
            return 0
        
    def unbalancedNodes(self, by=1):
        result = []
        self._get_unbalanced_nodes(self.root, by, result)
        return result

    def _get_unbalanced_nodes(self, node, by, result):
        if node is None:
            return
        
        balance = abs(self.nodeBalance(node))
        if balance > by:
            result.append(node.value)
        
        self._get_unbalanced_nodes(node.left_child, by, result)
        self._get_unbalanced_nodes(node.right_child, by, result)

