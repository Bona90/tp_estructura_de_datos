from programa.interfaces import IListarMensajes

# Clase Carpeta: contiene mensajes de un usuario.
class Carpeta(IListarMensajes):
    def __init__(self, nombre):
        self.set_nombre(nombre)  #  se usa doble protección.
        self.__mensajes = []

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ValueError("nombre debe ser una cadena de caracteres o no estar vacío.")
        self.__nombre = nombre

    def get_mensajes(self):
        return self.__mensajes

    # Métodos de clase Carpeta
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