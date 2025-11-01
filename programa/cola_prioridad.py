def obtener_prioridad(elemento):
    return elemento[0]    #    funcion auxiliar para obtener la prioridad del elemento.

class ColaPrioridad:
    def __init__(self):
        self.__cola = []    #   la cola almacena tuplas que inidican la prioridad y el elemento.
    
    def esta_vacia(self):
        return len(self.__cola) == 0    #    verifica si la cola no tiene elementos, devuelve True
    
    def agregar (self, elemento, prioridad):
        if not isinstance(prioridad, int) or prioridad < 1:
            raise ValueError("La prioridad debe ser un numero entero positivo.")
        self.__cola.append(prioridad, elemento)    #   agrega un elemento y reordena la lista según la prioridad, los elementos con prioridad  1 van primero.
        self.__cola.sort(key = obtener_prioridad)    #    mantiene la cola ordenada según la prioridad y con el método FIFO para los elementos de igual prioridad.
        
    def extraer_urgente(self):    #    devuelve y elimina el mensaje con la mayor prioridad.
        if self.esta_vacia():
            raise IndexError("No se pueden extraer elementos de una cola vacía.")
        return self.__cola.pop(0)[1]    #    pop(0) devuelve y elimina el primer elemento de la cola, [1] devuelve el elemento de la tupla correspondiente al mensaje.
    #    complejidad: O(n), n cantidad de elementos de la cola.
    
    def ver_proximo(self):    #    mmira el elemento más urgente sin eliminarlo.
        if self.esta_vacia():  
            return None
        return self.__cola[0][1]    #    accede al primer elemento de la cola [0] y devuelve el mensaje de la tupla [1].
    
    def __len__(self):
        return len(self.__cola)
    
        