import heapq
from collections import defaultdict

# Define una función para crear el árbol de Huffman
def huffman_tree(message):
    # Cuenta la frecuencia de cada carácter en el mensaje
    freq = defaultdict(int)
    for c in message:
        freq[c] += 1

    # Crea una lista de nodos hoja
    nodes = []
    for c in freq:
        nodes.append((freq[c], c))

    # Construye el árbol de Huffman combinando los nodos con menor frecuencia
    heapq.heapify(nodes)
    while len(nodes) > 1:
        freq1, c1 = heapq.heappop(nodes)
        freq2, c2 = heapq.heappop(nodes)
        heapq.heappush(nodes, (freq1 + freq2, (c1, c2)))

    # Devuelve la raíz del árbol de Huffman
    return nodes[0][1]

# Define una función para crear la tabla de códigos de Huffman
def huffman_table(tree):
    # Recorre el árbol de Huffman para asignar códigos a cada carácter
    table = {}
    def traverse(node, code):
        if isinstance(node, tuple):
            traverse(node[0], code + '0')
            traverse(node[1], code + '1')
        else:
            table[node] = code
    traverse(tree, '')
    return table

# Define una función para codificar un mensaje utilizando la tabla de códigos de Huffman
def huffman_encode(message, table):
    # Convierte el mensaje en una cadena de bits utilizando la tabla de códigos de Huffman
    encoded = ''
    for c in message:
        encoded += table[c]
    return encoded

# Define una función para decodificar un mensaje utilizando el árbol de Huffman
def huffman_decode(encoded, tree):
    # Decodifica la cadena de bits utilizando el árbol de Huffman
    message = ''
    node = tree
    for bit in encoded:
        if bit == '0':
            node = node[0]
        else:
            node = node[1]
        if isinstance(node, str):
            message += node
            node = tree
    return message

# Prueba el programa con un ejemplo de mensaje
message = 'Hola, mundo!'
tree = huffman_tree(message)
table = huffman_table(tree)
encoded = huffman_encode(message, table)
decoded = huffman_decode(encoded, tree)

# Muestra los resultados
print('Mensaje original:', message)
print('Tabla de códigos:', table)
print('Mensaje codificado:', encoded)
print('Mensaje decodificado:', decoded)
