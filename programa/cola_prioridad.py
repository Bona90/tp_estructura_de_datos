class Nodo:
    def __init__(self, elemento, prioridad):
        self.datos = (prioridad, elemento)    #    se define la tupla de los mensajes.
        self.siguiente = None    #    puntero al siguiente nodo.

class ColaPrioridad:
    def __init__(self):
        self.head = None    #    la cabeza es el primer nodo y será siempre el de mayor prioridad.
    
    def esta_vacia(self):
        return self.head is None    #    indica si no hay mensajes en la cola de prioridad. 
       
    def agregar (self, elemento, prioridad):
        nuevo_nodo = Nodo(elemento, prioridad)    #    agrega un elemento insertandolo en la posición correcta.
       #    si la cola está vacía o el elemento a insertar es de mayor prioridad se inserta en la cabeza.
        if self.esta_vacia() or prioridad < self.head.datos[0]:
           nuevo_nodo.siguiente = self.head
           self.head = nuevo_nodo
           return
       #    se busca la posición de inserción.
        actual = self.head
        while actual.siguiente is not None and actual.siguiente.datos[0] <= prioridad:
           actual = actual.siguiente   #    recorre la lista hasta enconetrar un nodo de prioridad mayor o igual o hasta llegar al final.
        #    insertar el nuevo nodo entre el actual y el siguiente.
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        
    def extraer_urgente(self):    #    devuelve y elimina el mensaje con la mayor prioridad.
        if self.esta_vacia():
            raise IndexError("No se pueden extraer elementos de una cola vacía.")
        #    elemento más urgente en la cabeza.
        elemento_urgente = self.head.datos[1]
        self.head = self.head.siguiente
        return elemento_urgente
    #    complejidad: O(n), n cantidad de elementos de la cola.
    
    def ver_proximo(self):    #    mmira el elemento más urgente sin eliminarlo.
        if self.esta_vacia():  
            return None
        return self.head.datos[1]    
    
        