from programa.interfaces import IListarMensajes

# Clase Carpeta: contiene mensajes de un usuario.
class Carpeta(IListarMensajes):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_mensajes(self):
        return self.__mensajes

    # Métodos de clase Carpeta
    def agregar_mensaje(self, mensaje): #Agrega un mensaje a la lista de la carpeta
        self.__mensajes.append(mensaje)

    def eliminar_mensaje(self, mensaje):    #Borra un mensaje de la carpeta (si está presente)
        if mensaje in self.__mensajes:
            self.__mensajes.remove(mensaje)

    def listar_mensajes(self):
        return [str(m) for m in self.__mensajes]    #Devuelve los mensajes de la carpeta en formato texto.