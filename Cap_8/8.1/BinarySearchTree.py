class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.cuenta = 1   # nueva propiedad para contar la cantidad de nodos con la misma clave

class BinarySearchTree:
    def __init__(self):
        self.raiz = None
    
    def _insertar(self, valor, nodo_actual):
        if valor == nodo_actual.valor:
            nodo_actual.cuenta += 1
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                altura_izquierda = self._altura(nodo_actual.izquierda)
                altura_derecha = self._altura(nodo_actual.derecha)
                if altura_izquierda <= altura_derecha:
                    self._insertar(valor, nodo_actual.izquierda)
                else:
                    self._insertar_nuevo_nivel(valor, nodo_actual)
        elif valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.derecha)

    def _insertar_nuevo_nivel(self, valor, nodo_actual):
        if nodo_actual.izquierda is None:
            nodo_actual.izquierda = Nodo(valor)
        else:
            altura_izquierda = self._altura(nodo_actual.izquierda)
            altura_derecha = self._altura(nodo_actual.derecha)
            if altura_izquierda <= altura_derecha:
                self._insertar_nuevo_nivel(valor, nodo_actual.izquierda)
            else:
                self._insertar_nuevo_nivel(valor, nodo_actual.derecha)
    def _insertar(self, valor, nodo_actual):
        if valor == nodo_actual.valor:
            nodo_actual.cuenta += 1
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                altura_izquierda = self._altura(nodo_actual.izquierda)
                altura_derecha = self._altura(nodo_actual.derecha)
                if altura_izquierda <= altura_derecha:
                    self._insertar(valor, nodo_actual.izquierda)
                else:
                    self._insertar_nuevo_nivel(valor, nodo_actual)
        elif valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.derecha)

    def _insertar_nuevo_nivel(self, valor, nodo_actual):
        if nodo_actual.izquierda is None:
            nodo_actual.izquierda = Nodo(valor)
        else:
            altura_izquierda = self._altura(nodo_actual.izquierda)
            altura_derecha = self._altura(nodo_actual.derecha)
            if altura_izquierda <= altura_derecha:
                self._insertar_nuevo_nivel(valor, nodo_actual.izquierda)
            else:
                 self._insertar_nuevo_nivel(valor, nodo_actual.derecha)

    
    def __find(self, valor):
        if self.raiz is not None:
            return self._find(valor, self.raiz)
        else:
            return None
    
    def _find(self, valor, nodo_actual):
        if valor == nodo_actual.valor:
            return nodo_actual
        elif valor < nodo_actual.valor and nodo_actual.izquierda is not None:
            return self._find(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor and nodo_actual.derecha is not None:
            return self._find(valor, nodo_actual.derecha)
    
    def eliminar(self, valor):
        nodo = self.__find(valor)
        if nodo is not None:
            if nodo.cuenta > 1:   # si hay más de un nodo con la misma clave, solo se reduce el contador
                nodo.cuenta -= 1
            else:
                self._eliminar_nodo(nodo)
    
    def _eliminar_nodo(self, nodo):
        if nodo.izquierda is None and nodo.derecha is None:
            nodo = None
        elif nodo.izquierda is None:
            nodo = nodo.derecha
        elif nodo.derecha is None:
            nodo = nodo.izquierda
        else:
            sucesor = self._encontrar_minimo(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.cuenta = sucesor.cuenta
            sucesor.cuenta = 1
            self._eliminar_nodo(sucesor)
    
    def _encontrar_minimo(self, nodo_actual):
        while nodo_actual.izquierda is not None:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual
    
    def imprimir_inorden(self):
        if self.raiz is not None:
            self._imprimir_inorden(self.raiz)
    
    def _imprimir_inorden(self, nodo_actual):
        if nodo_actual is not None:
            self._imprimir_inorden(nodo_actual.izquierda)
            for i in range(nodo_actual.cuenta):   # se imprime el valor varias veces según la cantidad de nodos con la misma clave
                print(str(nodo_actual.valor), end=' ')
            self._imprimir_inorden(nodo_actual.derecha)
    
    def imprimir_preorden(self):
        if self.raiz is not None:
            self._imprimir_preorden(self.raiz)
    
    def _imprimir_preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(str(nodo_actual.valor), end=' ')
            self._imprimir_preorden(nodo_actual.izquierda)
            self._imprimir_preorden(nodo_actual.derecha)
    
    def imprimir_postorden(self):
        if self.raiz is not None:
            self._imprimir_postorden(self.raiz)
    
    def _imprimir_postorden(self, nodo_actual):
        if nodo_actual is not None:
            self._imprimir_postorden(nodo_actual.izquierda)
            self._imprimir_postorden(nodo_actual.derecha)
            print(str(nodo_actual.valor), end=' ')

