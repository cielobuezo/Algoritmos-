def count_words(text):
    # Inicializamos una tabla hash vacía
    word_count = {}

    # Dividimos el texto en palabras
    words = text.split()

    # Recorremos todas las palabras
    for word in words:
        # Si la palabra ya está en la tabla hash, aumentamos su valor en 1
        if word in word_count:
            word_count[word] += 1
        # Si la palabra no está en la tabla hash, la agregamos con valor 1
        else:
            word_count[word] = 1

    # Recorremos la tabla hash completa para actualizar los recuentos
    for word, count in word_count.items():
        # Si la palabra ha sido vista antes, incrementamos su conteo en la tabla hash
        if word in word_count:
            word_count[word] += count - 1

    # Obtenemos el recuento total de palabras
    total_count = sum(word_count.values())

    # Devolvemos la tabla hash completa y el recuento total de palabras
    return word_count, total_count

# Ejemplo de uso
with open('miarchivo.txt', 'r') as file:
    texto = file.read()

conteo_palabras, total_count = count_words(texto)
print("Recuento total de palabras:", total_count)
for word, count in conteo_palabras.items():
    print(word, count)
