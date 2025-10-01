from programa.interfaces import IListarMensajes

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
    def agregar_mensaje(self, mensaje): #Agrega un mensaje a la lista de la carpeta
        self.__mensajes.append(mensaje)

    def eliminar_mensaje(self, mensaje):    #Borra un mensaje de la carpeta (si está presente)
        if mensaje in self.__mensajes:
            self.__mensajes.remove(mensaje)
        else:
            raise ValueError("El mensaje no está en la carpeta.")

    def listar_mensajes(self):
        if not self.__mensajes:
            return "La carpeta está vacía."
        return [str(m) for m in self.__mensajes]    #Devuelve los mensajes de la carpeta en formato texto.
    
    # Gestión de carpetas.
    def crear_subcarpeta(self, nombre):   #  se crea una subcarpeta.
        for subcarpeta in self.__subcarpetas:    #  se verifica que la carpeta no exista.
            if subcarpeta.get_nombre() == nombre:
                raise ValueError("La carpeta ya existe.")
        nueva = Carpeta(nombre)    #  se crea una instancia de Carpeta con el nombre de la subcarpeta.
        nueva.set_padre(self)    #  asigna como padre la carpeta actual
        self.__subcarpetas.append(nueva)
        return nueva
    
    def agregar_subcarpeta(self, carpeta):    #  se agrega una subcarpeta existente.
        if not isinstance(carpeta, Carpeta):    #  se verifica que sea instancia de Carpeta.
            raise TypeError("El objeto debe ser una carpeta.")
        for subcarpeta in self.__subcarpetas:
            if subcarpeta.get_nombre() == carpeta.get_nombre():   #  se evita dos "hijos" con igual nombre.
                raise ValueError("Ya existe una subcarpeta con ese nombre en este subnivel.")
        padre_anterior = carpeta.get_padre()
        if padre_anterior is not None:
            padre_anterior.__subcarpetas.remove(carpeta)  #  si existe se remueve el padre anterior.
        carpeta.set_padre(self)    #  se asigna el nuevo padre.
        self.__subcarpetas.append(carpeta)   #  se agrega la subcarpeta.
        
    def eliminar_subcarpeta(self, nombre):
        for subcarpeta in self.__subcarpetas:
            if subcarpeta.get_nombre() == nombre:    #  si existe la subcarpeta la elimina.
                self.__subcarpetas.remove(subcarpeta)
                subcarpeta.set_padre(None)    #  cambia el padre de la subcarpeta.
                return
        raise ValueError("No existe una subcarpeta con ese nombre en este nivel.")