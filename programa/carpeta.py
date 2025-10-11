from programa.interfaces import IListarMensajes
from programa.mensaje import Mensaje

# Clase Carpeta: contiene mensajes de un usuario.
class Carpeta(IListarMensajes):
    def __init__(self, nombre, padre = None):
        self.set_nombre(nombre)  #  nombre del Nodo.
        self.__mensajes = []
        self.__subcarpetas = []   #  lista de objetos Carpeta.
        self.set_padre(padre)   #  carpeta padre.

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ValueError("nombre debe ser una cadena de caracteres o no estar vacío.")
        self.__nombre = nombre

    def get_mensajes(self):
        return self.__mensajes
    
    def get_subcarpetas(self):
        return self.__subcarpetas

    def get_padre(self):
        return self.__padre

    def set_padre(self, padre):
        self.__padre = padre    #  puede ser una Carpeta o None

    # Gestión de mensajes.
    def agregar_mensaje(self, mensaje): #  Agrega un mensaje a la lista de la carpeta
        if not isinstance(mensaje, Mensaje):
            raise TypeError("Solo se pueden agregar objetos del tipo Mensaje.")
        self.__mensajes.append(mensaje)
        #  Complejidad: O(1), agrega un elemento al final de la lista.

    def eliminar_mensaje(self, mensaje):    #  Borra un mensaje de la carpeta (si está presente)
        if mensaje in self.__mensajes:
            self.__mensajes.remove(mensaje)
        else:
            raise ValueError("El mensaje no está en la carpeta.")
        #   Complejidad: O(m) m = numero de mensajes en la carpeta.
        
    def listar_mensajes(self):
        if not self.__mensajes:
            return "La carpeta está vacía."
        return [str(m) for m in self.__mensajes]    #  Devuelve los mensajes de la carpeta en formato texto.
        #   Complejidad: O(m) m = numero de mensajes en la carpeta.
    
    def mover_mensaje(self, mensaje, carpeta_destino):
        if not isinstance(carpeta_destino, Carpeta):    #   Si la carpeta de destino no es de tipo carpeta arroja un error.
            raise TypeError("carpeta destino debe ser una Carpeta.")
        if mensaje not in self.__mensajes:      #  Verifica que el mensaje esté en la carpeta.
            raise ValueError("El mensaje no esta en esta carpeta.")
        self.__mensajes.remove(mensaje)    #   Remueve el mensaje de la carpeta actual
        carpeta_destino.agregar_mensaje(mensaje)   #   Agrega el mensaje a la carpeta de destino.
        #   Complejidad: O(m) + O(1) m = numero de mensajes en la carpeta. O(n) corresponde a eliminar mensaje, O(1) a agregar en la carpeta.
    
    # Gestión de carpetas.
    def crear_subcarpeta(self, nombre):   #  Se crea una subcarpeta.
        for subcarpeta in self.__subcarpetas:    #  Se verifica que la carpeta no exista.
            if subcarpeta.get_nombre() == nombre:
                raise ValueError("La carpeta ya existe.")
        nueva = Carpeta(nombre)    #  Se crea una instancia de Carpeta con el nombre de la subcarpeta.
        nueva.set_padre(self)    #  Asigna como padre la carpeta actual
        self.__subcarpetas.append(nueva)
        return nueva
        #   Complejidad: O(n) n = numero de subcarpetas.
    
    def agregar_subcarpeta(self, carpeta):    #  Se agrega una subcarpeta existente.
        if not isinstance(carpeta, Carpeta):    #  Se verifica que sea instancia de Carpeta.
            raise TypeError("El objeto debe ser una carpeta.")
        for subcarpeta in self.__subcarpetas:
            if subcarpeta.get_nombre() == carpeta.get_nombre():   #  Se evita dos "hijos" con igual nombre.
                raise ValueError("Ya existe una subcarpeta con ese nombre en este subnivel.")
        padre_anterior = carpeta.get_padre()
        if padre_anterior is not None:
            padre_anterior.__subcarpetas.remove(carpeta)  #  Si existe se remueve el padre anterior.
        carpeta.set_padre(self)    #  Se asigna el nuevo padre.
        self.__subcarpetas.append(carpeta)   #  Se agrega la subcarpeta.
        #   Complejidad: O(n) n = numero de subcarpetas.
        
    def eliminar_subcarpeta(self, nombre):
        for subcarpeta in self.__subcarpetas:
            if subcarpeta.get_nombre() == nombre:    #  Si existe la subcarpeta la elimina.
                self.__subcarpetas.remove(subcarpeta)
                subcarpeta.set_padre(None)    #  Cambia el padre de la subcarpeta.
                return
        raise ValueError("No existe una subcarpeta con ese nombre en este nivel.")
        #   Complejidad: O(n) n = numero de subcarpetas.
    
    # Busqueda recursiva.
    #  Busqueda de mensajes por remitente en todo el árbol.
    def busqueda_por_remitente(self, remitente):
        encontrados = [m for m in self.__mensajes if m.get_remitente() == remitente] #   Crea una lista con los mensajes del remitente.
        for subcarpeta in self.__subcarpetas:   #   Recorre todo el arbol
            encontrados.extend(subcarpeta.busqueda_por_remitente(remitente))
        if len(encontrados) == 0:
            return []
        return encontrados
        #   Complejidad: O(m+n) m = numero de mensajes en la carpeta y n= numero de subcarpetas.
    
    #   Busqueda de mensajes por asutno en todo el árbol.
    def busqueda_por_asunto(self, asunto):
        encontrados = [m for m in self.__mensajes if asunto.lower() in m.get_asunto().lower()]  #   Crea una lista con los mensajes que contienen el asunto.
        for subcarpeta in self.__subcarpetas:
            encontrados.extend(subcarpeta.busqueda_por_asunto(asunto))  #  Llamada recursiva.
        if len(encontrados) == 0:
            return []
        return encontrados   
        #   Complejidad: O(m+n) m = numero de mensajes en la carpeta y n= numero de subcarpetas. 
